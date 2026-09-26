document.addEventListener('DOMContentLoaded', () => {
  const header = document.querySelector('.site-header');
  const toggle = document.querySelector('.menu-toggle');
  const themeToggle = document.querySelector('.theme-toggle');
  const links = document.querySelector('.nav-links');
  const topButton = document.querySelector('.back-to-top');
  const navLinks = [...document.querySelectorAll('.nav-links a[href^="#"]')];
  const sections = [document.getElementById('home'), ...document.querySelectorAll('main section[id]')];

  const applyTheme = (theme) => {
    const isLight = theme === 'light';
    document.body.classList.toggle('light-mode', isLight);
    localStorage.setItem('theme', theme);

    if (themeToggle) {
      themeToggle.setAttribute('aria-pressed', String(isLight));
      const icon = themeToggle.querySelector('i');
      if (icon) {
        icon.className = isLight ? 'fa-solid fa-lightbulb' : 'fa-regular fa-lightbulb';
      }
    }
  };

  const savedTheme = localStorage.getItem('theme');
  const preferredTheme = savedTheme || 'dark';
  applyTheme(preferredTheme);

  themeToggle?.addEventListener('click', () => {
    const nextTheme = document.body.classList.contains('light-mode') ? 'dark' : 'light';
    applyTheme(nextTheme);
  });

  toggle?.addEventListener('click', () => {
    const open = links.classList.toggle('open');
    toggle.setAttribute('aria-expanded', String(open));
    toggle.innerHTML = open ? '<i class="fa-solid fa-xmark"></i>' : '<i class="fa-solid fa-bars"></i>';
  });
  navLinks.forEach(link => link.addEventListener('click', () => links.classList.remove('open')));

  const onScroll = () => {
    header.classList.toggle('scrolled', window.scrollY > 20);
    topButton.classList.toggle('show', window.scrollY > 500);

    let current = 'home';
    for (const element of sections) {
      if (element && window.scrollY >= element.offsetTop - 140) {
        current = element.id || 'home';
      }
    }

    navLinks.forEach(link => link.classList.toggle('active', link.getAttribute('href') === `#${current}`));
  };

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
  topButton?.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

  const observer = new IntersectionObserver(entries => entries.forEach(entry => entry.isIntersecting && entry.target.classList.add('visible')), { threshold: .12 });
  document.querySelectorAll('.reveal').forEach(element => observer.observe(element));

  document.querySelectorAll('.certificate-toggle').forEach(button => {
    button.addEventListener('click', () => {
      const card = button.closest('.certificate-card');
      const expanded = card.classList.toggle('is-expanded');
      button.setAttribute('aria-expanded', String(expanded));
      button.querySelector('.toggle-label').textContent = expanded ? 'Hide certificate' : 'View certificate';
    });
  });

  document.getElementById('year').textContent = new Date().getFullYear();
});
