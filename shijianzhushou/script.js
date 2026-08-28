const header = document.querySelector('[data-header]');
const menuButton = document.querySelector('.menu-button');
const mobileMenu = document.querySelector('.mobile-menu');

window.addEventListener('scroll', () => {
  header?.classList.toggle('scrolled', window.scrollY > 20);
}, { passive: true });

menuButton?.addEventListener('click', () => {
  const open = menuButton.getAttribute('aria-expanded') === 'true';
  menuButton.setAttribute('aria-expanded', String(!open));
  menuButton.setAttribute('aria-label', open ? '打开导航' : '关闭导航');
  mobileMenu?.classList.toggle('open', !open);
});

mobileMenu?.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => {
    menuButton?.setAttribute('aria-expanded', 'false');
    mobileMenu.classList.remove('open');
  });
});

const revealObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });
document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

const number = document.querySelector('[data-count]');
if (number) {
  const countObserver = new IntersectionObserver(entries => {
    if (!entries[0].isIntersecting) return;
    const target = Number(number.dataset.count);
    let value = 0;
    const timer = setInterval(() => {
      value += 1;
      number.textContent = `${value}`;
      if (value >= target) clearInterval(timer);
    }, 120);
    countObserver.disconnect();
  });
  countObserver.observe(number);
}

function pad(n) { return String(n).padStart(2, '0'); }

function updateClocks() {
  const now = new Date();
  const h = now.getHours();
  const m = now.getMinutes();
  const s = now.getSeconds();
  const ms = now.getMilliseconds();

  document.getElementById('hh').textContent = pad(h);
  document.getElementById('mm').textContent = pad(m);
  document.getElementById('ss').textContent = pad(s);

  const weekdays = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六'];
  const dateEl = document.getElementById('liveDate');
  if (dateEl) {
    dateEl.textContent = `${now.getFullYear()} 年 ${now.getMonth() + 1} 月 ${now.getDate()} 日 ${weekdays[now.getDay()]}`;
  }

  const mini = document.getElementById('miniClock');
  if (mini) mini.textContent = `${pad(h)}:${pad(m)}`;

  const tz = document.getElementById('tzLabel');
  if (tz) {
    const offset = -now.getTimezoneOffset() / 60;
    tz.textContent = `UTC${offset >= 0 ? '+' : ''}${offset}`;
  }

  const hourDeg = (h % 12) * 30 + m * 0.5;
  const minDeg = m * 6 + s * 0.1;
  const secDeg = s * 6 + ms * 0.006;

  const handHour = document.getElementById('handHour');
  const handMinute = document.getElementById('handMinute');
  const handSecond = document.getElementById('handSecond');
  if (handHour) handHour.style.transform = `rotate(${hourDeg}deg)`;
  if (handMinute) handMinute.style.transform = `rotate(${minDeg}deg)`;
  if (handSecond) handSecond.style.transform = `rotate(${secDeg}deg)`;
}

updateClocks();
setInterval(updateClocks, 50);

const clockFace = document.getElementById('clockFace');
if (clockFace) {
  for (let i = 0; i < 60; i++) {
    const tick = document.createElement('div');
    tick.className = i % 5 === 0 ? 'clock-tick major' : 'clock-tick';
    tick.style.transform = `rotate(${i * 6}deg)`;
    clockFace.appendChild(tick);
  }
}

const starsContainer = document.getElementById('stars');
if (starsContainer && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
  for (let i = 0; i < 40; i++) {
    const star = document.createElement('div');
    star.className = 'star';
    star.style.left = `${Math.random() * 100}%`;
    star.style.top = `${Math.random() * 100}%`;
    star.style.animationDelay = `${Math.random() * 3}s`;
    star.style.animationDuration = `${2 + Math.random() * 3}s`;
    starsContainer.appendChild(star);
  }
}

document.querySelectorAll('[data-year]').forEach(el => {
  el.textContent = new Date().getFullYear();
});
