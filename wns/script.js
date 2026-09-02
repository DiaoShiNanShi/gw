const rail = document.querySelector('[data-rail]');
const railToggle = document.querySelector('[data-rail-toggle]');
const railBackdrop = document.querySelector('[data-rail-backdrop]');
const railLinks = document.querySelectorAll('[data-rail] a[href^="#"]');

function closeRail() {
  rail?.classList.remove('open');
  railBackdrop?.classList.remove('open');
  railToggle?.setAttribute('aria-expanded', 'false');
}

railToggle?.addEventListener('click', () => {
  const open = rail?.classList.toggle('open');
  railBackdrop?.classList.toggle('open', open);
  railToggle.setAttribute('aria-expanded', String(open));
});

railBackdrop?.addEventListener('click', closeRail);
railLinks.forEach(link => link.addEventListener('click', closeRail));

const sections = [...document.querySelectorAll('[data-section]')];
const navLinks = [...document.querySelectorAll('[data-rail] a[href^="#"]')];

if (sections.length && navLinks.length) {
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      const id = entry.target.id;
      navLinks.forEach(link => {
        link.classList.toggle('active', link.getAttribute('href') === `#${id}`);
      });
    });
  }, { rootMargin: '-30% 0px -55% 0px', threshold: 0 });

  sections.forEach(section => observer.observe(section));
}
