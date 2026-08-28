document.documentElement.classList.add('js');

/* ── Header & Nav ── */
const header = document.querySelector('.site-header');
const menuBtn = document.querySelector('.menu-btn');
const navLinks = document.querySelector('.nav-links');
const navItems = document.querySelectorAll('[data-nav]');
const sections = navItems.length
  ? [...navItems].map(a => document.querySelector(a.getAttribute('href'))).filter(Boolean)
  : [];

window.addEventListener('scroll', () => {
  header?.classList.toggle('scrolled', window.scrollY > 20);

  const scrollPos = window.scrollY + 120;
  sections.forEach((sec, i) => {
    if (sec.offsetTop <= scrollPos && sec.offsetTop + sec.offsetHeight > scrollPos) {
      navItems.forEach(n => n.classList.remove('active'));
      navItems[i]?.classList.add('active');
    }
  });
}, { passive: true });

menuBtn?.addEventListener('click', () => navLinks?.classList.toggle('open'));
navLinks?.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => navLinks.classList.remove('open'));
});

/* ── Cursor glow ── */
const glow = document.querySelector('.cursor-glow');
if (glow && matchMedia('(pointer:fine)').matches) {
  document.addEventListener('mousemove', e => {
    glow.style.left = e.clientX + 'px';
    glow.style.top = e.clientY + 'px';
  }, { passive: true });
}

/* ── Particle canvas ── */
const canvas = document.getElementById('particles');
if (canvas && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
  const ctx = canvas.getContext('2d');
  let w, h, dots = [];

  function resize() {
    w = canvas.width = window.innerWidth;
    h = canvas.height = window.innerHeight;
  }
  resize();
  window.addEventListener('resize', resize);

  for (let i = 0; i < 60; i++) {
    dots.push({
      x: Math.random() * w,
      y: Math.random() * h,
      r: Math.random() * 1.5 + .5,
      dx: (Math.random() - .5) * .3,
      dy: (Math.random() - .5) * .3,
    });
  }

  function drawParticles() {
    ctx.clearRect(0, 0, w, h);
    dots.forEach(d => {
      d.x += d.dx;
      d.y += d.dy;
      if (d.x < 0 || d.x > w) d.dx *= -1;
      if (d.y < 0 || d.y > h) d.dy *= -1;
      ctx.beginPath();
      ctx.arc(d.x, d.y, d.r, 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(100,210,255,.35)';
      ctx.fill();
    });
    dots.forEach((a, i) => {
      dots.slice(i + 1).forEach(b => {
        const dist = Math.hypot(a.x - b.x, a.y - b.y);
        if (dist < 120) {
          ctx.beginPath();
          ctx.moveTo(a.x, a.y);
          ctx.lineTo(b.x, b.y);
          ctx.strokeStyle = `rgba(100,210,255,${.12 * (1 - dist / 120)})`;
          ctx.stroke();
        }
      });
    });
    requestAnimationFrame(drawParticles);
  }
  drawParticles();
}

/* ── Typewriter ── */
const tw = document.getElementById('typewriter');
if (tw) {
  const phrases = ['iOS 开发工程师', 'Swift · Flutter · AI', 'App 全链路交付'];
  let pi = 0, ci = 0, deleting = false;

  function typeLoop() {
    const current = phrases[pi];
    tw.textContent = deleting
      ? current.slice(0, ci--)
      : current.slice(0, ci++);

    if (!deleting && ci > current.length) {
      setTimeout(() => { deleting = true; typeLoop(); }, 2000);
      return;
    }
    if (deleting && ci < 0) {
      deleting = false;
      ci = 0;
      pi = (pi + 1) % phrases.length;
    }
    setTimeout(typeLoop, deleting ? 40 : 80);
  }
  typeLoop();
}

/* ── Reveal on scroll ── */
const revealObs = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      revealObs.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });
document.querySelectorAll('.reveal').forEach(el => revealObs.observe(el));

/* ── Counter animation ── */
function animateCount(el, target) {
  let current = 0;
  const step = Math.max(1, Math.floor(target / 30));
  const timer = setInterval(() => {
    current += step;
    if (current >= target) { current = target; clearInterval(timer); }
    el.textContent = current + (target === 10 || target === 6 ? '+' : '');
  }, 40);
}

const countObs = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (!entry.isIntersecting) return;
    const el = entry.target;
    const target = Number(el.dataset.count);
    if (target) animateCount(el, target);
    countObs.unobserve(el);
  });
}, { threshold: 0.5 });
document.querySelectorAll('[data-count]').forEach(el => countObs.observe(el));

/* ── Phone skill bars ── */
const phoneObs = new IntersectionObserver(entries => {
  if (!entries[0].isIntersecting) return;
  document.querySelectorAll('.skill-bar .bar span').forEach(bar => {
    bar.style.width = bar.dataset.width + '%';
  });
  phoneObs.disconnect();
}, { threshold: 0.3 });
const phoneStage = document.querySelector('.phone-stage');
if (phoneStage) phoneObs.observe(phoneStage);

/* ── Skill level bars ── */
const levelObs = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) entry.target.classList.add('visible');
  });
}, { threshold: 0.5 });
document.querySelectorAll('.skill-card').forEach(el => levelObs.observe(el));

/* ── Skill tabs ── */
document.querySelectorAll('.skill-tab').forEach(tab => {
  tab.addEventListener('click', () => {
    document.querySelectorAll('.skill-tab').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.skill-panel').forEach(p => p.classList.remove('active'));
    tab.classList.add('active');
    document.querySelector(`[data-panel="${tab.dataset.tab}"]`)?.classList.add('active');
  });
});

/* ── Experience accordion ── */
document.querySelectorAll('[data-exp]').forEach(card => {
  const btn = card.querySelector('.exp-toggle');
  btn?.addEventListener('click', () => {
    const isActive = card.classList.contains('active');
    document.querySelectorAll('[data-exp]').forEach(c => {
      c.classList.remove('active');
      c.querySelector('.exp-toggle')?.setAttribute('aria-expanded', 'false');
    });
    if (!isActive) {
      card.classList.add('active');
      btn.setAttribute('aria-expanded', 'true');
    }
  });
});

/* ── Project filters ── */
document.querySelectorAll('.filter').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.filter').forEach(f => f.classList.remove('active'));
    btn.classList.add('active');
    const cat = btn.dataset.filter;
    document.querySelectorAll('.project-item').forEach(item => {
      const match = cat === 'all' || item.dataset.cat === cat;
      item.classList.toggle('hidden', !match);
      if (match) {
        item.style.animation = 'none';
        item.offsetHeight;
        item.style.animation = 'fadeUp .4s cubic-bezier(.22,1,.36,1)';
      }
    });
  });
});

/* ── 3D tilt effect ── */
function bindTilt(el) {
  if (!matchMedia('(pointer:fine)').matches) return;
  el.addEventListener('mousemove', e => {
    const rect = el.getBoundingClientRect();
    const x = (e.clientX - rect.left) / rect.width - .5;
    const y = (e.clientY - rect.top) / rect.height - .5;
    el.style.transform = `perspective(800px) rotateY(${x * 10}deg) rotateX(${-y * 10}deg) translateY(-4px)`;
  });
  el.addEventListener('mouseleave', () => { el.style.transform = ''; });
}
document.querySelectorAll('[data-tilt]').forEach(el => {
  const phone = el.querySelector('.phone');
  if (phone) {
    el.addEventListener('mousemove', e => {
      const rect = el.getBoundingClientRect();
      const x = (e.clientX - rect.left) / rect.width - .5;
      const y = (e.clientY - rect.top) / rect.height - .5;
      phone.style.transform = `rotateY(${x * 12}deg) rotateX(${-y * 8}deg)`;
    });
    el.addEventListener('mouseleave', () => { phone.style.transform = ''; });
  }
});
document.querySelectorAll('.tilt').forEach(bindTilt);

/* ── Magnetic buttons ── */
document.querySelectorAll('.magnetic').forEach(btn => {
  if (!matchMedia('(pointer:fine)').matches) return;
  btn.addEventListener('mousemove', e => {
    const rect = btn.getBoundingClientRect();
    const x = e.clientX - rect.left - rect.width / 2;
    const y = e.clientY - rect.top - rect.height / 2;
    btn.style.transform = `translate(${x * .15}px, ${y * .15}px)`;
  });
  btn.addEventListener('mouseleave', () => { btn.style.transform = ''; });
});

document.getElementById('year').textContent = new Date().getFullYear();
