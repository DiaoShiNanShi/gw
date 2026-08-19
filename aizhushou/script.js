const header = document.querySelector('[data-header]');
const menuButton = document.querySelector('.menu-button');
const mobileMenu = document.querySelector('.mobile-menu');

window.addEventListener('scroll', () => header?.classList.toggle('scrolled', window.scrollY > 20), { passive: true });

menuButton?.addEventListener('click', () => {
  const open = menuButton.getAttribute('aria-expanded') === 'true';
  menuButton.setAttribute('aria-expanded', String(!open));
  menuButton.setAttribute('aria-label', open ? '打开导航' : '关闭导航');
  mobileMenu?.classList.toggle('open', !open);
});

mobileMenu?.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
  menuButton?.setAttribute('aria-expanded', 'false');
  mobileMenu.classList.remove('open');
}));

const revealObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });
document.querySelectorAll('.reveal').forEach(element => revealObserver.observe(element));

const number = document.querySelector('[data-count]');
if (number) {
  const countObserver = new IntersectionObserver(entries => {
    if (!entries[0].isIntersecting) return;
    const target = Number(number.dataset.count);
    let value = 0;
    const timer = setInterval(() => {
      value += 1;
      number.textContent = `${value}+`;
      if (value >= target) clearInterval(timer);
    }, 90);
    countObserver.disconnect();
  });
  countObserver.observe(number);
}

const stage = document.querySelector('[data-tilt]');
const phone = stage?.querySelector('.phone');
if (stage && phone && matchMedia('(pointer:fine)').matches && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
  stage.addEventListener('pointermove', event => {
    const rect = stage.getBoundingClientRect();
    const x = (event.clientX - rect.left) / rect.width - .5;
    const y = (event.clientY - rect.top) / rect.height - .5;
    phone.style.transform = `rotateY(${x * 11}deg) rotateX(${-y * 8}deg) rotate(4deg)`;
  });
  stage.addEventListener('pointerleave', () => { phone.style.transform = 'rotate(4deg)'; });
}

const toast = document.querySelector('.demo-toast');
let toastTimer;
document.querySelectorAll('.quick').forEach(button => button.addEventListener('click', () => {
  document.querySelectorAll('.quick').forEach(item => item.classList.remove('active'));
  button.classList.add('active');
  if (!toast) return;
  toast.textContent = `已选择：${button.dataset.demo}`;
  toast.classList.add('show');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => toast.classList.remove('show'), 1400);
}));

document.querySelectorAll('[data-year]').forEach(element => { element.textContent = new Date().getFullYear(); });
