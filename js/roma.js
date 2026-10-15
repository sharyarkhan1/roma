(function ($) {
    'use strict';

    var landing = document.getElementById('romaLanding');
    var manView = document.getElementById('romaMan');
    var womanView = document.getElementById('romaWoman');
    var currentView = null;

    function hideAllViews() {
        $('.roma-view').removeClass('active');
    }

    function initTestimonialSlider($view) {
        $view.find('.testimonials-slider .swiper').each(function () {
            if (this.swiper) {
                this.swiper.update();
                return;
            }
            new Swiper(this, {
                slidesPerView: 1,
                speed: 1500,
                spaceBetween: 30,
                loop: true,
                autoplay: { delay: 5000 },
                breakpoints: {
                    768: { slidesPerView: 1 },
                    1024: { slidesPerView: 2 }
                }
            });
        });
    }

    function initSlickNav($view) {
        var $menu = $view.find('.nav-menu-wrapper > ul').first();
        var $responsive = $view.find('.responsive-menu').first();

        if (!$menu.length || !$responsive.length) return;

        $responsive.empty();

        if ($menu.data('slicknav')) {
            try { $menu.slicknav('destroy'); } catch (e) {}
        }

        $menu.slicknav({
            label: '',
            prependTo: $responsive
        });
    }

    function refreshView($view) {
        initSlickNav($view);
        initTestimonialSlider($view);

        if ($.fn.parallaxie && $(window).width() > 768) {
            $view.find('.parallaxie').parallaxie({ speed: 0.55, offset: 0 });
        }

        if (typeof WOW !== 'undefined') {
            new WOW({ live: false }).init();
        }

        if ($.fn.magnificPopup) {
            $view.find('.gallery-items').magnificPopup({
                delegate: 'a',
                type: 'image',
                closeOnContentClick: false,
                closeBtnInside: false,
                mainClass: 'mfp-with-zoom',
                image: { verticalFit: true },
                gallery: { enabled: true },
                zoom: {
                    enabled: true,
                    duration: 300,
                    opener: function (element) {
                        return element.find('img');
                    }
                }
            });
        }

        if ($('.popup-video').length) {
            $view.find('.popup-video').magnificPopup({
                type: 'iframe',
                mainClass: 'mfp-fade',
                removalDelay: 160,
                preloader: false,
                fixedContentPos: true
            });
        }
    }

    function showView(view) {
        hideAllViews();
        landing.classList.add('hidden');
        var $view = $(view);
        $view.addClass('active');
        currentView = view;
        window.scrollTo(0, 0);
        document.body.style.overflow = '';
        refreshView($view);
    }

    function goHome() {
        hideAllViews();
        landing.classList.remove('hidden');
        currentView = null;
        window.scrollTo(0, 0);
    }

    $('#romaSelectMan').on('click', function (e) {
        e.preventDefault();
        showView(manView);
    });

    $('#romaSelectWoman').on('click', function (e) {
        e.preventDefault();
        showView(womanView);
    });

    $(document).on('click', '[data-roma-home]', function (e) {
        e.preventDefault();
        goHome();
    });

    $(document).on('click', '[data-roma-switch]', function (e) {
        e.preventDefault();
        var target = $(this).data('roma-switch');
        if (target === 'man') showView(manView);
        if (target === 'woman') showView(womanView);
    });

    $(document).on('click', '.roma-view.active a[href^="#"]', function (e) {
        var href = $(this).attr('href');
        if (!href || href === '#') return;

        var $target = $(href);
        if (!$target.length || !$target.closest('.roma-view.active').length) return;

        e.preventDefault();
        var headerH = $('.roma-view.active .header-sticky.active').length ? 90 : 0;
        $('html, body').animate({
            scrollTop: $target.offset().top - headerH
        }, 600);
    });

    /* Appointment Popup */
    $(document).off('click.appointmentPopup', '.appointment-popup');

    $(document).on('click.appointmentPopup', '.appointment-popup', function (e) {
        e.preventDefault();

        $.magnificPopup.open({
            items: {
                src: '#appointment-popup'
            },
            type: 'inline',
            mainClass: 'mfp-fade',
            removalDelay: 160,
            closeBtnInside: true,
            fixedContentPos: true
        });
    });

    /* Appointment Form Submit */

    $(document).off('submit.appointmentForm', '#appointmentForm');

    $(document).on('submit.appointmentForm', '#appointmentForm', function (e) {
        e.preventDefault();

        var $form = $(this);
        var $button = $('#appointmentSubmit');
        var $message = $('#appointmentMsg');

        $button.prop('disabled', true).text('Sending...');
        $message.removeClass('success error').hide().text('');

        $.ajax({
            url: 'send-appointment.php',
            type: 'POST',
            data: $form.serialize(),
            dataType: 'json',

            success: function (response) {

                if (response.success) {

                    $form[0].reset();

                    $message
                        .removeClass('error')
                        .addClass('success')
                        .text(response.message)
                        .show();

                    $button.prop('disabled', false).text('Submit Appointment');

                } else {

                    $message
                        .removeClass('success')
                        .addClass('error')
                        .text(response.message)
                        .show();

                    $button.prop('disabled', false).text('Submit Appointment');
                }
            },

            error: function () {

                $message
                    .removeClass('success')
                    .addClass('error')
                    .text('Something went wrong. Please try again.')
                    .show();

                $button.prop('disabled', false).text('Submit Appointment');
            }
        });
    });

})(jQuery);


