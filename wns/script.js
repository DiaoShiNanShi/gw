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
      navLinks.forEach(link => {
        link.classList.toggle('active', link.getAttribute('href') === `#${entry.target.id}`);
      });
    });
  }, { rootMargin: '-30% 0px -55% 0px', threshold: 0 });
  sections.forEach(section => observer.observe(section));
}

const revealObserver = new IntersectionObserver(entries => {
  entries.forEach((entry, i) => {
    if (!entry.isIntersecting) return;
    entry.target.style.transitionDelay = `${(entry.target.dataset.delay || 0) * 80}ms`;
    entry.target.classList.add('visible');
    revealObserver.unobserve(entry.target);
  });
}, { threshold: 0.1 });
document.querySelectorAll('.reveal').forEach((el, i) => {
  el.dataset.delay = i % 6;
  revealObserver.observe(el);
});

document.querySelectorAll('.luminous-wrap').forEach((wrap, i) => {
  wrap.style.setProperty('--glow-angle', `${i * 72}deg`);
  wrap.addEventListener('mouseenter', () => wrap.classList.add('is-lit'));
  wrap.addEventListener('mouseleave', () => wrap.classList.remove('is-lit'));
});

const track = document.querySelector('.filmstrip-track');
if (track) {
  let isDown = false;
  let startX = 0;
  let scrollLeft = 0;

  track.addEventListener('mousedown', e => {
    isDown = true;
    track.classList.add('is-dragging');
    startX = e.pageX - track.offsetLeft;
    scrollLeft = track.scrollLeft;
  });
  track.addEventListener('mouseleave', () => {
    isDown = false;
    track.classList.remove('is-dragging');
  });
  track.addEventListener('mouseup', () => {
    isDown = false;
    track.classList.remove('is-dragging');
  });
  track.addEventListener('mousemove', e => {
    if (!isDown) return;
    e.preventDefault();
    const x = e.pageX - track.offsetLeft;
    track.scrollLeft = scrollLeft - (x - startX) * 1.2;
  });
}

const board = document.querySelector('.status-board');
if (board && matchMedia('(pointer:fine)').matches && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
  board.addEventListener('pointermove', e => {
    const rect = board.getBoundingClientRect();
    const x = ((e.clientX - rect.left) / rect.width - 0.5) * 20;
    const y = ((e.clientY - rect.top) / rect.height - 0.5) * 12;
    document.querySelectorAll('.luminous-orb').forEach((orb, i) => {
      const factor = i === 0 ? 1 : -0.6;
      orb.style.transform = `translate(${x * factor}px, ${y * factor}px)`;
    });
  });
}
