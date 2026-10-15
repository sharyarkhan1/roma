#!/usr/bin/env python3
"""Generate ROMA simple one-page salon site — Man & Woman views."""

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1">
    <meta name="description" content="ROMA Hair Salon — Premium grooming for Men & Women across the UK. Book your appointment today.">
    <meta name="keywords" content="ROMA, hair salon, barber, men, women, London, UK">
    <title>ROMA — Hair Salon | UK</title>
    <link rel="shortcut icon" type="image/x-icon" href="images/favicon.png">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap" rel="stylesheet">
    <link href="css/bootstrap.min.css" rel="stylesheet" media="screen">
    <link href="css/slicknav.min.css" rel="stylesheet">
    <link rel="stylesheet" href="css/swiper-bundle.min.css">
    <link href="css/all.min.css" rel="stylesheet" media="screen">
    <link href="css/animate.css" rel="stylesheet">
    <link rel="stylesheet" href="css/magnific-popup.css">
    <link rel="stylesheet" href="css/mousecursor.css">
    <link href="css/custom.css" rel="stylesheet" media="screen">
    <link href="css/roma.css" rel="stylesheet" media="screen">
</head>
<body>
'''

LANDING = '''
    <div class="preloader">
        <div class="loading-container">
            <div class="loading"></div>
            <div id="loading-icon"><img src="images/logo-white.svg" alt="ROMA"></div>
        </div>
    </div>

    <div class="roma-landing" id="romaLanding">
        <div class="roma-landing-header">
            <img src="images/logo-white.svg" alt="ROMA">
        </div>
        <div class="roma-split">
            <a href="#" class="roma-split-panel roma-split-man" id="romaSelectMan">
                <div class="roma-split-content">
                    <p class="roma-split-label">Explore</p>
                    <h2 class="roma-split-title">Man</h2>
                    <span class="roma-split-arrow"><i class="fa-solid fa-arrow-right"></i></span>
                </div>
            </a>
            <div class="roma-split-divider"></div>
            <a href="#" class="roma-split-panel roma-split-woman" id="romaSelectWoman">
                <div class="roma-split-content">
                    <p class="roma-split-label">Explore</p>
                    <h2 class="roma-split-title">Woman</h2>
                    <span class="roma-split-arrow"><i class="fa-solid fa-arrow-right"></i></span>
                </div>
            </a>
        </div>
        <p class="roma-landing-tagline">Grooming &middot; Style &middot; London</p>
    </div>
'''

WA_LINK = 'https://wa.me/442033862015?text=Hi%20ROMA%2C%20I%27d%20like%20to%20book%20an%20appointment.'

FOOT = '''
    <script src="js/jquery-3.7.1.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/validator.min.js"></script>
    <script src="js/jquery.slicknav.js"></script>
    <script src="js/swiper-bundle.min.js"></script>
    <script src="js/jquery.waypoints.min.js"></script>
    <script src="js/jquery.counterup.min.js"></script>
    <script src="js/jquery.magnific-popup.min.js"></script>
    <script src="js/SmoothScroll.js"></script>
    <script src="js/parallaxie.js"></script>
    <script src="js/gsap.min.js"></script>
    <script src="js/magiccursor.js"></script>
    <script src="js/SplitText.min.js"></script>
    <script src="js/ScrollTrigger.min.js"></script>
    <script src="js/jquery.mb.YTPlayer.min.js"></script>
    <script src="js/wow.min.js"></script>
    <script src="js/function.js"></script>
    <script src="js/roma.js"></script>
</body>
</html>
'''

MAN = {
    'id': 'romaMan', 'prefix': 'man', 'switch_to': 'woman', 'switch_label': 'Woman',
    'logo': 'images/logo-white.svg',
    'menu_id': 'menu-man',
    'hero_sub': 'ROMA For Men · United Kingdom',
    'hero_title': 'Sharp Cuts. Clean Style. Pure Confidence.',
    'hero_desc': 'Premium barbering and grooming for the modern British gentleman. Walk in looking good, walk out looking great.',
    'hero_type': 'video',
    'about_img1': 'images/about-us-image-1.jpg',
    'about_img2': 'images/about-us-image-2.jpg',
    'about_sub': 'About Us',
    'about_title': 'London\'s Finest Men\'s Grooming Destination',
    'about_p': 'At ROMA Men, we combine classic British barbering with modern techniques. Our expert barbers deliver precision fades, clean shaves, and styles that match your personality — all in a sleek black & white atmosphere in the heart of London.',
    'about_item1': 'Expert Barbers',
    'about_item1_p': 'Trained professionals skilled in fades, cuts, beard styling and traditional hot towel shaves.',
    'about_item2': 'Premium Products',
    'about_item2_p': 'Top-quality pomades, oils and aftershaves for a finish that lasts all day.',
    'services_sub': 'Our Services',
    'services_title': 'Grooming Services Built for Men',
    'services': [
        ('Haircut & Fade', 'icon-service-item-1.svg', 'Precision cuts and fades tailored to your face shape and lifestyle.'),
        ('Beard Trim & Shape', 'icon-service-item-2.svg', 'Expert beard grooming — clean lines, perfect shape, conditioned finish.'),
        ('Hot Towel Shave', 'icon-service-item-3.svg', 'Traditional straight-razor shave with hot towels for the smoothest skin.'),
        ('Hair Styling', 'icon-service-item-4.svg', 'Professional styling with premium products for any occasion.'),
    ],
    'why_title': 'Why Men Choose ROMA',
    'why_p': 'We are not just a barbershop — we are your grooming partner in the UK. Hygienic tools, a relaxed vibe, and results you can trust every single visit.',
    'pricing': [
        ('Haircut', 'pricing-item-image-1.jpg', '£25', 'Classic or modern cut styled to perfection'),
        ('Fade / Taper', 'pricing-item-image-4.jpg', '£30', 'Skin fade, taper fade or burst fade'),
        ('Beard Grooming', 'pricing-item-image-3.jpg', '£15', 'Trim, shape and condition your beard'),
        ('Hot Towel Shave', 'pricing-item-image-6.jpg', '£22', 'Luxury straight-razor shave experience'),
        ('Hair + Beard Combo', 'pricing-item-image-8.jpg', '£38', 'Complete grooming package — best value'),
        ('Facial & Cleanup', 'pricing-item-image-2.jpg', '£35', 'Refresh your skin with a deep cleanse'),
    ],
    'testimonials': [
        ('James Mitchell', 'Business Owner', 'our-testimonials-image-1.jpg',
         'Best fade in London, hands down. The barbers at ROMA really know what they are doing. Clean shop, fair prices.'),
        ('Oliver Hughes', 'Software Engineer', 'our-testimonials-image-3.jpg',
         'I have been coming here for six months. Consistent quality every time. The hot towel shave is something else.'),
        ('William Carter', 'Student', 'our-testimonials-image-2.jpg',
         'Great atmosphere and friendly staff. They listened to exactly what I wanted and nailed it. Highly recommend.'),
    ],
    'faqs': [
        ('Do I need an appointment?', 'Walk-ins are welcome, but we recommend booking ahead on weekends and bank holidays to avoid wait times.'),
        ('How long does a haircut take?', 'A standard haircut takes 30–40 minutes. Fades and combos may take up to an hour.'),
        ('What products do you use?', 'We use premium brands including American Crew, Reuzel, and Proraso among others.'),
    ],
    'footer_services': ['Haircut & Fade', 'Beard Grooming', 'Hot Towel Shave', 'Hair Styling', 'Facial & Cleanup'],
    'gallery_imgs': [f'images/gallery-{i}.jpeg' for i in range(1, 14)],
}

WOMAN = {
    'id': 'romaWoman', 'prefix': 'woman', 'switch_to': 'man', 'switch_label': 'Man',
    'logo': 'images/logo-white.svg',
    'menu_id': 'menu-woman',
    'hero_sub': 'ROMA For Women · United Kingdom',
    'hero_title': 'Beautiful Hair. Confident You. Every Day.',
    'hero_desc': 'Luxurious hair care and styling by expert stylists. From everyday elegance to bridal glamour — we make you shine.',
    'hero_type': 'image',
    'hero_img': 'images/woman-hero.jpg',
    'about_img1': 'images/post-2.jpg',
    'about_img2': 'images/post-3.jpg',
    'about_sub': 'About Us',
    'about_title': 'Where Every Woman Feels Beautiful',
    'about_p': 'ROMA Women is a premium UK salon designed for you. Our talented stylists specialise in cuts, colour, treatments and bridal hair — creating looks that celebrate your unique beauty in a calm, elegant space.',
    'about_item1': 'Expert Stylists',
    'about_item1_p': 'Stylists trained in the latest cuts, colours, balayage and bridal techniques.',
    'about_item2': 'Luxury Treatments',
    'about_item2_p': 'Keratin, deep conditioning and scalp therapies with salon-grade products.',
    'services_sub': 'Our Services',
    'services_title': 'Hair Services Crafted for Women',
    'services': [
        ('Cut & Styling', 'icon-service-item-1.svg', 'Flattering cuts and blow-dry styling for every hair type and face shape.'),
        ('Hair Colouring', 'icon-service-item-2.svg', 'Full colour, highlights, balayage and root touch-ups with premium dyes.'),
        ('Keratin Treatment', 'icon-service-item-3.svg', 'Smooth, frizz-free hair that lasts for months with our keratin therapy.'),
        ('Bridal & Party Hair', 'icon-service-item-4.svg', 'Stunning updos and styles for weddings, events and special occasions.'),
    ],
    'why_title': 'Why Women Love ROMA',
    'why_p': 'We understand that your hair is your crown. That is why every visit includes a personal consultation, gentle care, and results that make you feel amazing.',
    'pricing': [
        ('Haircut & Blow Dry', 'pricing-item-image-1.jpg', '£45', 'Cut and styled finish for everyday elegance'),
        ('Root Touch-Up', 'pricing-item-image-5.jpg', '£55', 'Cover greys with seamless colour matching'),
        ('Full Hair Colour', 'pricing-item-image-3.jpg', '£85', 'Complete colour transformation'),
        ('Highlights / Balayage', 'pricing-item-image-7.jpg', '£120', 'Natural-looking dimension and depth'),
        ('Keratin Treatment', 'pricing-item-image-2.jpg', '£150', 'Long-lasting smooth and silky hair'),
        ('Bridal Hair Package', 'pricing-item-image-6.jpg', '£250', 'Trial + wedding day styling included'),
    ],
    'testimonials': [
        ('Emily Roberts', 'Teacher', 'our-testimonials-image-2.jpg',
         'My balayage turned out absolutely gorgeous. The team at ROMA really understand colour. Best salon experience I have had in London.'),
        ('Sophie Clarke', 'Bride', 'our-testimonials-image-1.jpg',
         'They did my bridal hair and it was flawless. I felt like a princess. Thank you ROMA team!'),
        ('Charlotte Evans', 'Doctor', 'our-testimonials-image-3.jpg',
         'Clean, professional and so relaxing. My keratin treatment changed my hair completely. Cannot recommend enough.'),
    ],
    'faqs': [
        ('Do I need an appointment?', 'Yes, we recommend booking especially for colour and bridal services. Walk-ins accepted for cuts when available.'),
        ('How long does colouring take?', 'Root touch-ups take 1–2 hours. Full colour or balayage can take 3–4 hours.'),
        ('Do you offer bridal packages?', 'Yes! We offer bridal trials, wedding day styling, and party packages. Contact us for details.'),
    ],
    'footer_services': ['Cut & Styling', 'Hair Colouring', 'Keratin Treatment', 'Bridal Hair', 'Blow Dry & Updos'],
    'gallery_imgs': [f'images/gallery-{i}.jpeg' for i in range(1, 14)],
}


def render_view(c):
    p = c['prefix']
    wa = WA_LINK
    delays = ['', '0.2s', '0.4s', '0.6s', '0.8s', '1s']

    # Hero
    if c.get('hero_type') == 'video':
        hero_bg = '''<div class="hero-bg-video">
            <video autoplay muted playsinline loop><source src="media/hairline-hero-video.mp4" type="video/mp4"></video>
        </div>'''
    else:
        hero_bg = f'''<div class="hero-bg-video">
            <img src="{c['hero_img']}" alt="ROMA Women Salon">
        </div>'''

    services_html = ''
    for i, (title, icon, desc) in enumerate(c['services']):
        d = f' data-wow-delay="{delays[i]}"' if i else ''
        services_html += f'''
                <div class="col-xl-3 col-md-6">
                    <div class="service-item wow fadeInUp"{d}>
                        <div class="service-item-header"><h2><a href="#{p}-contact">{title}</a></h2></div>
                        <div class="icon-box"><img src="images/{icon}" alt=""></div>
                        <div class="service-item-body">
                            <div class="service-item-content"><p>{desc}</p></div>
                            <div class="service-item-btn"><a href="{wa}" class="readmore-btn" target="_blank" rel="noopener noreferrer">Book Now</a></div>
                        </div>
                    </div>
                </div>'''

    pricing_html = ''
    for i, (title, img, price, desc) in enumerate(c['pricing']):
        d = f' data-wow-delay="{delays[i]}"' if i else ''
        pricing_html += f'''
                        <div class="pricing-item wow fadeInUp"{d}>
                            <div class="pricing-item-image"><figure class="image-anime"><img src="images/{img}" alt=""></figure></div>
                            <div class="pricing-item-body">
                                <div class="pricing-item-title"><h2>{title}</h2><hr><h3>{price}</h3></div>
                                <div class="pricing-item-content"><p>{desc}</p></div>
                            </div>
                        </div>'''

    slides_html = ''
    for name, role, img, text in c['testimonials']:
        slides_html += f'''
                                <div class="swiper-slide">
                                    <div class="testimonials-item">
                                        <div class="testimonials-item-image"><figure class="image-anime"><img src="images/{img}" alt=""></figure></div>
                                        <div class="testimonials-item-body">
                                            <div class="testimonials-item-content">
                                                <span class="testimonials-item-rating-star"><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i></span>
                                                <p>"{text}"</p>
                                            </div>
                                            <div class="testimonials-item-author">
                                                <div class="testimonials-item-author-content"><h2>{name}</h2><p>{role}</p></div>
                                                <div class="testimonial-item-quote"><img src="images/testimonial-quote.svg" alt=""></div>
                                            </div>
                                        </div>
                                    </div>
                                </div>'''

    faq_html = ''
    for i, (q, a) in enumerate(c['faqs']):
        show = 'show' if i == 0 else ''
        expanded = 'true' if i == 0 else 'false'
        collapsed = '' if i == 0 else 'collapsed'
        d = f' data-wow-delay="{delays[i]}"' if i else ''
        faq_html += f'''
                        <div class="accordion-item wow fadeInUp"{d}>
                            <h2 class="accordion-header"><button class="accordion-button {collapsed}" type="button" data-bs-toggle="collapse" data-bs-target="#{p}-faq{i}" aria-expanded="{expanded}">{q}</button></h2>
                            <div id="{p}-faq{i}" class="accordion-collapse collapse {show}" data-bs-parent="#accordion-{p}"><div class="accordion-body"><p>{a}</p></div></div>
                        </div>'''

    gallery_blocks = ''
    for img in c['gallery_imgs']:
        gallery_blocks += f'''
                <div class="photo-gallery">
                    <a href="{img}" data-cursor-text="View"><figure class="image-anime"><img src="{img}" alt=""></figure></a>
                </div>'''

    footer_svc = '\n'.join(f'<li><a href="#{p}-services">{s}</a></li>' for s in c['footer_services'])

    return f'''
    <div class="roma-view" id="{c['id']}">
    <header class="main-header active-sticky-header">
        <div class="header-sticky">
            <nav class="navbar navbar-expand-lg">
                <div class="container">
                    <a class="navbar-brand" href="#" data-roma-home aria-label="ROMA Home">
                        <img src="{c['logo']}" alt="ROMA Hair Salon" width="140" height="45">
                    </a>
                    <div class="collapse navbar-collapse main-menu">
                        <div class="nav-menu-wrapper">
                            <ul class="navbar-nav mr-auto" id="{c['menu_id']}">
                                <li class="nav-item"><a class="nav-link" href="#{p}-hero">Home</a></li>
                                <li class="nav-item"><a class="nav-link" href="#{p}-about">About</a></li>
                                <li class="nav-item"><a class="nav-link" href="#{p}-services">Services</a></li>
                                <li class="nav-item"><a class="nav-link" href="#{p}-pricing">Pricing</a></li>
                                <li class="nav-item"><a class="nav-link" href="#{p}-contact">Contact</a></li>
                            </ul>
                        </div>
                        <div class="header-btn">
                            <a href="#" class="roma-switch-btn" data-roma-switch="{c['switch_to']}">{c['switch_label']}</a>
                            <a href="{wa}" class="btn-default btn-highlighted" target="_blank" rel="noopener noreferrer">Book an Appointment</a>
                        </div>
                    </div>
                    <div class="navbar-toggle"></div>
                </div>
            </nav>
            <div class="responsive-menu"></div>
        </div>
    </header>

    <div class="hero dark-section parallaxie" id="{p}-hero">
        {hero_bg}
        <div class="container">
            <div class="row align-items-end">
                <div class="col-xl-7">
                    <div class="hero-content">
                        <div class="section-title">
                            <span class="section-sub-title wow fadeInUp">{c['hero_sub']}</span>
                            <h1 class="text-anime-style-3" data-cursor="-opaque">{c['hero_title']}</h1>
                            <p class="wow fadeInUp" data-wow-delay="0.15s" style="color:rgba(255,255,255,0.8);margin-top:20px;line-height:1.7;">{c['hero_desc']}</p>
                        </div>
                        <div class="hero-btn wow fadeInUp" data-wow-delay="0.3s">
                            <a href="{wa}" class="btn-default btn-highlighted" target="_blank" rel="noopener noreferrer">Book an Appointment</a>
                        </div>
                    </div>
                </div>
                <div class="col-xl-5">
                    <div class="hero-working-hours wow fadeInUp" data-wow-delay="0.4s">
                        <div class="hero-working-hours-header">
                            <div class="icon-box"><img src="images/icon-clock.svg" alt=""></div>
                            <div class="hero-working-hours-title"><h2>Opening Hours:</h2></div>
                        </div>
                        <div class="hero-working-hour-list">
                            <ul>
                                <li>Monday - Friday <span>9:00 AM - 8:00 PM</span></li>
                                <li>Saturday <span>9:00 AM - 7:00 PM</span></li>
                                <li>Sunday <span>10:00 AM - 6:00 PM</span></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="about-us" id="{p}-about">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-xl-6">
                    <div class="about-us-image-box wow fadeInUp">
                        <div class="about-us-image-box-1">
                            <div class="about-us-image"><figure class="image-anime"><img src="{c['about_img1']}" alt=""></figure></div>
                        </div>
                        <div class="about-us-image-box-2">
                            <div class="contact-us-circle"><a href="#{p}-contact"><img src="images/contact-us-circle.svg" alt=""></a></div>
                            <div class="about-us-image"><figure class="image-anime"><img src="{c['about_img2']}" alt=""></figure></div>
                        </div>
                    </div>
                </div>
                <div class="col-xl-6">
                    <div class="about-us-content">
                        <div class="section-title">
                            <span class="section-sub-title wow fadeInUp">{c['about_sub']}</span>
                            <h2 class="text-anime-style-3" data-cursor="-opaque">{c['about_title']}</h2>
                            <p class="wow fadeInUp" data-wow-delay="0.2s">{c['about_p']}</p>
                        </div>
                        <div class="about-us-item-list">
                            <div class="about-us-item wow fadeInUp" data-wow-delay="0.4s">
                                <div class="icon-box"><img src="images/icon-about-item-1.svg" alt=""></div>
                                <div class="about-us-item-content"><h3>{c['about_item1']}</h3><p>{c['about_item1_p']}</p></div>
                            </div>
                            <div class="about-us-item wow fadeInUp" data-wow-delay="0.6s">
                                <div class="icon-box"><img src="images/icon-about-item-2.svg" alt=""></div>
                                <div class="about-us-item-content"><h3>{c['about_item2']}</h3><p>{c['about_item2_p']}</p></div>
                            </div>
                        </div>
                        <div class="about-us-body wow fadeInUp" data-wow-delay="0.8s">
                            <div class="about-us-btn"><a href="#{p}-services" class="btn-default">View Services</a></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="our-services dark-section" id="{p}-services">
        <div class="container">
            <div class="row section-row"><div class="col-lg-12">
                <div class="section-title section-title-center">
                    <span class="section-sub-title wow fadeInUp">{c['services_sub']}</span>
                    <h2 class="text-anime-style-3" data-cursor="-opaque">{c['services_title']}</h2>
                </div>
            </div></div>
            <div class="row">{services_html}</div>
        </div>
    </div>

    <div class="why-choose-us">
        <div class="container">
            <div class="row align-items-center">
                <div class="col-xl-7">
                    <div class="why-choose-content">
                        <div class="section-title">
                            <span class="section-sub-title wow fadeInUp">Why Choose ROMA</span>
                            <h2 class="text-anime-style-3" data-cursor="-opaque">{c['why_title']}</h2>
                            <p class="wow fadeInUp" data-wow-delay="0.2s">{c['why_p']}</p>
                        </div>
                        <div class="why-choose-list wow fadeInUp" data-wow-delay="0.4s">
                            <ul>
                                <li>Skilled & Certified Professionals</li>
                                <li>100% Hygienic & Sterilized Tools</li>
                                <li>Premium Quality Products</li>
                                <li>Comfortable & Elegant Atmosphere</li>
                            </ul>
                        </div>
                        <div class="why-choose-body wow fadeInUp" data-wow-delay="0.6s">
                            <div class="why-choose-btn"><a href="{wa}" class="btn-default" target="_blank" rel="noopener noreferrer">Book Appointment</a></div>
                            <div class="why-choose-contact-box">
                                <div class="icon-box"><img src="images/icon-headphone-white.svg" alt=""></div>
                                <div class="why-choose-contact-content"><p>Call Us Now!</p><h3><a href="tel:+442033862015">+44 (20) 3386 2015</a></h3></div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-xl-5">
                    <div class="why-choose-image"><figure><img src="images/why-choose-us-image.png" alt=""></figure></div>
                </div>
            </div>
        </div>
    </div>

    <div class="intro-video" id="{p}-video">
        <div class="container-fluid">
            <div class="row">
                <div class="col-lg-12">
                    <div class="intro-video-box">
                        <div class="intro-bg-video">
                            <video autoplay muted playsinline loop><source src="{c.get('intro_video', 'media/hairline-intro-video.mp4')}" type="video/mp4"></video>
                        </div>
                        <div class="intro-video-circle">
                            <a href="{c.get('video_url', 'https://www.youtube.com/watch?v=Y-x0efG1seA')}" class="popup-video" data-cursor-text="Play">
                                <img src="images/watch-video-circle.svg" alt="Watch Our Video">
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="our-pricing dark-section" id="{p}-pricing">
        <div class="container">
            <div class="row section-row"><div class="col-lg-12">
                <div class="section-title section-title-center">
                    <span class="section-sub-title wow fadeInUp">Pricing</span>
                    <h2 class="text-anime-style-3" data-cursor="-opaque">Transparent & Fair Prices</h2>
                    <p class="wow fadeInUp" data-wow-delay="0.2s">Quality service at prices that respect your budget. No hidden charges.</p>
                </div>
            </div></div>
            <div class="row"><div class="col-lg-12">
                <div class="pricing-item-list">{pricing_html}</div>
            </div></div>
        </div>
    </div>

    <div class="our-scrolling-ticker">
        <div class="scrolling-ticker-box gallery-items page-gallery-box">
            <div class="scrolling-content">{gallery_blocks}</div>
            <div class="scrolling-content">{gallery_blocks}</div>
        </div>
    </div>

    <div class="our-testimonials" id="{p}-testimonials">
        <div class="container">
            <div class="row section-row"><div class="col-lg-12">
                <div class="section-title section-title-center">
                    <span class="section-sub-title wow fadeInUp">Testimonials</span>
                    <h2 class="text-anime-style-3" data-cursor="-opaque">What Our Clients Say</h2>
                </div>
            </div></div>
            <div class="row"><div class="col-lg-12">
                <div class="testimonials-slider">
                    <div class="swiper"><div class="swiper-wrapper" data-cursor-text="Drag">{slides_html}</div></div>
                </div>
            </div></div>
        </div>
    </div>

    <div class="our-faqs dark-section parallaxie" id="{p}-faq">
        <div class="container">
            <div class="row">
                <div class="col-xl-6">
                    <div class="faqs-content">
                        <div class="section-title">
                            <span class="section-sub-title wow fadeInUp">FAQ</span>
                            <h2 class="text-anime-style-3" data-cursor="-opaque">Got Questions? We Have Answers</h2>
                        </div>
                        <div class="faqs-content-btn wow fadeInUp" data-wow-delay="0.4s">
                            <a href="#{p}-contact" class="btn-default btn-highlighted">Contact Us</a>
                        </div>
                    </div>
                </div>
                <div class="col-xl-6">
                    <div class="faq-accordion" id="accordion-{p}">{faq_html}</div>
                </div>
            </div>
        </div>
    </div>

    <footer class="main-footer dark-section" id="{p}-contact">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <div class="footer-logo"><hr><img src="images/logo-white.svg" alt="ROMA"><hr></div>
                </div>
                <div class="col-xl-4">
                    <div class="footer-contact-info">
                        <ul>
                            <li>12 Regent Street, London, W1B 5AH, United Kingdom</li>
                            <li><span>Phone:</span><a href="tel:+442033862015">+44 (20) 3386 2015</a></li>
                            <li><span>Email:</span><a href="mailto:hello@roma.co.uk">hello@roma.co.uk</a></li>
                            <li><span>Hours:</span> Mon–Sat 9:00 AM – 8:00 PM · Sun 10:00 AM – 6:00 PM</li>
                        </ul>
                    </div>
                </div>
                <div class="col-xl-8">
                    <div class="footer-links-box">
                        <div class="footer-links">
                            <h2>Quick Links</h2>
                            <ul>
                                <li><a href="#" data-roma-home>Select Man / Woman</a></li>
                                <li><a href="#{p}-about">About</a></li>
                                <li><a href="#{p}-services">Services</a></li>
                                <li><a href="#{p}-pricing">Pricing</a></li>
                            </ul>
                        </div>
                        <div class="footer-links">
                            <h2>Our Services</h2>
                            <ul>{footer_svc}</ul>
                        </div>
                        <div class="footer-links footer-newsletter-box">
                            <h2>Book Appointment</h2>
                            <p class="footer-book-text">Message us on WhatsApp to schedule your visit.</p>
                            <a href="{wa}" class="btn-default btn-highlighted" target="_blank" rel="noopener noreferrer">Book on WhatsApp</a>
                            <div class="footer-social-links" style="margin-top:25px;">
                                <h3>Follow Us:</h3>
                                <ul>
                                    <li><a href="#"><i class="fa-brands fa-facebook-f"></i></a></li>
                                    <li><a href="#"><i class="fa-brands fa-instagram"></i></a></li>
                                    <li><a href="#"><i class="fa-brands fa-whatsapp"></i></a></li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="footer-copyright">
            <div class="container">
                <div class="row align-items-center">
                    <div class="col-md-6">
                        <div class="footer-copyright-text footer-copyright-left">
                            <p>Copyright &copy; 2026 ROMA Hair Salon. All Rights Reserved.</p>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="footer-copyright-text footer-copyright-right">
                            <p>Designed &amp; Developed By <a href="https://creativewebsitesolution.co.uk/" target="_blank" rel="noopener noreferrer">Creative Website Solution</a></p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </footer>
    </div>
'''


def main():
    html = HEAD + LANDING + render_view(MAN) + render_view(WOMAN) + FOOT
    path = '/Applications/XAMPP/xamppfiles/htdocs/roma/index.html'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Generated {path} ({len(html.splitlines())} lines)')


if __name__ == '__main__':
    main()
