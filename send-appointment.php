<?php

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require __DIR__ . '/PHPMailer/src/Exception.php';
require __DIR__ . '/PHPMailer/src/PHPMailer.php';
require __DIR__ . '/PHPMailer/src/SMTP.php';

header('Content-Type: application/json; charset=UTF-8');


// --------------------------------------------------
// Only allow POST requests
// --------------------------------------------------

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    echo json_encode([
        'success' => false,
        'message' => 'Invalid request.'
    ]);
    exit;
}


// --------------------------------------------------
// Get form data
// --------------------------------------------------

$name    = trim($_POST['name'] ?? '');
$email   = trim($_POST['email'] ?? '');
$phone   = trim($_POST['phone'] ?? '');
$message = trim($_POST['message'] ?? '');


// --------------------------------------------------
// Validate required fields
// --------------------------------------------------

if ($name === '' || $email === '' || $phone === '' || $message === '') {

    echo json_encode([
        'success' => false,
        'message' => 'Please fill in all required fields.'
    ]);

    exit;
}


// --------------------------------------------------
// Validate email
// --------------------------------------------------

if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {

    echo json_encode([
        'success' => false,
        'message' => 'Please enter a valid email address.'
    ]);

    exit;
}


// --------------------------------------------------
// PHPMailer
// --------------------------------------------------

$mail = new PHPMailer(true);

try {


    // Load deployment-only SMTP credentials from an ignored local file or environment.
    $localSmtpConfig = [];
    $localConfigPath = __DIR__ . '/config.local.php';
    if (is_file($localConfigPath)) {
        $loadedConfig = require $localConfigPath;
        if (is_array($loadedConfig)) {
            $localSmtpConfig = $loadedConfig;
        }
    }
    $smtpUsername = isset($localSmtpConfig['smtp_username'])
        ? $localSmtpConfig['smtp_username']
        : (getenv('ROMA_SMTP_USERNAME') ?: '');
    $smtpPassword = isset($localSmtpConfig['smtp_password'])
        ? $localSmtpConfig['smtp_password']
        : (getenv('ROMA_SMTP_PASSWORD') ?: '');
    if ($smtpUsername === '' || $smtpPassword === '') {
        throw new RuntimeException('SMTP credentials are not configured.');
    }

    // SMTP settings
$mail->isSMTP();

    $mail->Host       = 'smtp.gmail.com';
    $mail->SMTPAuth   = true;

    // Gmail account
    $mail->Username   = $smtpUsername;
    $mail->Password   = $smtpPassword;

    // Gmail SMTP - TLS
    $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
    $mail->Port       = 587;


    // --------------------------------------------------
    // Sender
    // --------------------------------------------------

    $mail->setFrom(
        'roma.hair.shops@gmail.com',
        'ROMA Hair Shop Website'
    );


    // --------------------------------------------------
    // Receiver
    // --------------------------------------------------

    $mail->addAddress(
        'roma.hair.shops@gmail.com',
        'ROMA Hair Shop'
    );


    // --------------------------------------------------
    // Reply to customer
    // --------------------------------------------------

    $mail->addReplyTo(
        $email,
        $name
    );


    // --------------------------------------------------
    // Email format
    // --------------------------------------------------

    $mail->isHTML(true);

    $mail->Subject = 'New Appointment Request - ROMA Hair Shop';


    // --------------------------------------------------
    // Email body
    // --------------------------------------------------

    $safeName = htmlspecialchars(
        $name,
        ENT_QUOTES,
        'UTF-8'
    );

    $safeEmail = htmlspecialchars(
        $email,
        ENT_QUOTES,
        'UTF-8'
    );

    $safePhone = htmlspecialchars(
        $phone,
        ENT_QUOTES,
        'UTF-8'
    );

    $safeMessage = nl2br(
        htmlspecialchars(
            $message,
            ENT_QUOTES,
            'UTF-8'
        )
    );


    $mail->Body = '
        <div style="font-family: Arial, sans-serif; line-height: 1.6;">

            <h2>New Appointment Request</h2>

            <hr>

            <p>
                <strong>Name:</strong><br>
                ' . $safeName . '
            </p>

            <p>
                <strong>Email:</strong><br>
                ' . $safeEmail . '
            </p>

            <p>
                <strong>Phone:</strong><br>
                ' . $safePhone . '
            </p>

            <p>
                <strong>Message:</strong><br>
                ' . $safeMessage . '
            </p>

            <hr>

            <p>
                <small>
                    This appointment request was submitted from the ROMA Hair Shop website.
                </small>
            </p>

        </div>
    ';


    // --------------------------------------------------
    // Plain text version
    // --------------------------------------------------

    $mail->AltBody =
        "New Appointment Request\n\n" .
        "Name: " . $name . "\n" .
        "Email: " . $email . "\n" .
        "Phone: " . $phone . "\n\n" .
        "Message:\n" . $message;


    // --------------------------------------------------
    // Send email
    // --------------------------------------------------

    $mail->send();


    // --------------------------------------------------
    // Success response
    // --------------------------------------------------

    echo json_encode([
        'success' => true,
        'message' => 'Thank you! Your appointment request has been sent successfully.'
    ]);

} catch (Exception $e) {

    // Log actual error for debugging
    error_log(
        'PHPMailer Error: ' . $mail->ErrorInfo
    );


    // Send safe message to browser
    echo json_encode([
        'success' => false,
        'message' => 'Unable to send your request right now. Please try again later.'
    ]);
}