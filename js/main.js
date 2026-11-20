/* Interactions jQuery & JavaScript - Conformes aux critères Séance 6 IIT */
$(document).ready(function () {
  // 1. Effet Spotlight qui suit la souris (Brittany Chiang style)
  $(window).on('pointermove', function (e) {
    document.documentElement.style.setProperty('--mouse-x', `${e.clientX}px`);
    document.documentElement.style.setProperty('--mouse-y', `${e.clientY}px`);
  });

  // 2. Thème Switcher (Dark / Light) avec persistance localStorage
  const storedTheme = localStorage.getItem('portfolio-theme') || 'dark';

  function setTheme(theme) {
    if (theme === 'light') {
      $('html').attr('data-theme', 'light');
    } else {
      $('html').removeAttr('data-theme');
    }
    localStorage.setItem('portfolio-theme', theme);
  }

  setTheme(storedTheme);

  $('#theme-toggle').on('click', function () {
    const currentTheme = $('html').attr('data-theme') === 'light' ? 'light' : 'dark';
    const nextTheme = currentTheme === 'light' ? 'dark' : 'light';
    setTheme(nextTheme);
  });

  // 3. Navigation Active State on Scroll (Intersection Observer)
  const sections = document.querySelectorAll('section[id]');
  const navLinks = $('.nav-link');

  const observerOptions = {
    root: null,
    rootMargin: '-20% 0px -70% 0px',
    threshold: 0
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.getAttribute('id');
        navLinks.each(function () {
          if ($(this).attr('href') === `#${id}`) {
            $(this).addClass('active');
          } else {
            $(this).removeClass('active');
          }
        });
      }
    });
  }, observerOptions);

  sections.forEach(section => observer.observe(section));

  // 4. Formulaire de contact (Gestion front-end avec jQuery)
  $('#contact-form').on('submit', function (e) {
    if (!$(this).attr('action')) {
      e.preventDefault();
      const name = $('#id_name').val().trim();
      $('#contact-feedback')
        .text(`Merci ${name} ! Votre message a bien été envoyé. Je vous répondrai dans les plus brefs délais.`)
        .addClass('success')
        .fadeIn(300);

      this.reset();
      setTimeout(() => {
        $('#contact-feedback').fadeOut(400);
      }, 5000);
    }
  });

  // 5. Animation dynamique au clic sur les logos des technologies
  $('.skills-block .tag-badge').on('click', function () {
    const $badge = $(this);
    $badge.removeClass('badge-pop');
    void this.offsetWidth;
    $badge.addClass('badge-pop');

    const $icon = $badge.find('i');
    if ($icon.length) {
      $('.tech-fullscreen-logo').remove();

      const $logoWrapper = $('<div class="tech-fullscreen-logo"></div>');
      const $giantIcon = $icon.clone();
      $logoWrapper.append($giantIcon);
      $('body').append($logoWrapper);

      setTimeout(() => {
        $logoWrapper.remove();
      }, 1300);
    }
  });
});
