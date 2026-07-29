// ============================================================
//  Fusion Beauty Studio — Main Script
// ============================================================

// ---- Navbar: scroll effect ----
const navbar   = document.getElementById('navbar');
const floatBtn = document.getElementById('floatBook');

window.addEventListener('scroll', () => {
  floatBtn.classList.toggle('visible', window.scrollY > 400);
});

// ---- Mobile hamburger ----
const hamburger = document.getElementById('hamburger');
const navLinks  = document.getElementById('navLinks');

function closeMobileMenu() {
  navLinks.classList.remove('open');
  hamburger.classList.remove('menu-open');
}

hamburger.addEventListener('click', () => {
  const isOpen = navLinks.classList.toggle('open');
  hamburger.classList.toggle('menu-open', isOpen);
});

// Close when any nav link is clicked
navLinks.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', closeMobileMenu);
});

// ---- Active nav link on scroll ----
const sections = document.querySelectorAll('section[id]');
const links    = document.querySelectorAll('.nav-links a');

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      links.forEach(l => l.classList.remove('active'));
      const active = document.querySelector(`.nav-links a[href="#${entry.target.id}"]`);
      if (active) active.classList.add('active');
    }
  });
}, { threshold: 0.4 });

sections.forEach(s => observer.observe(s));

// ---- Scroll-in animations ----
const animateEls = document.querySelectorAll(
  '.service-card, .why-card, .testimonial-card, .about-grid, .contact-grid, .booking-wrap'
);

const fadeObserver = new IntersectionObserver(entries => {
  entries.forEach((entry, i) => {
    if (entry.isIntersecting) {
      setTimeout(() => {
        entry.target.classList.add('animated');
      }, (entry.target.dataset.delay || 0));
      fadeObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });

animateEls.forEach((el, i) => {
  el.classList.add('fade-up');
  el.dataset.delay = (i % 3) * 100;
  fadeObserver.observe(el);
});

// ---- Booking form submission ----
function handleBooking(e) {
  e.preventDefault();

  const form    = document.getElementById('bookingForm');
  const success = document.getElementById('bookingSuccess');
  const btn     = form.querySelector('button[type="submit"]');

  // Simple loading state
  btn.textContent = 'Sending…';
  btn.disabled    = true;

  // Simulate a short send delay (replace with actual API/email integration)
  setTimeout(() => {
    form.style.display    = 'none';
    success.style.display = 'block';

    // Scroll into view
    success.scrollIntoView({ behavior: 'smooth', block: 'center' });

    // NOTE: To actually send form data, integrate with a service such as:
    //   - Formspree (formspree.io) — just change the form action
    //   - EmailJS (emailjs.com) — free tier works well
    //   - Your booking platform's API (Vagaro, Booksy, Jane App, etc.)
  }, 1200);
}

// ---- Set minimum date on date picker to today ----
const dateInput = document.getElementById('preferredDate');
if (dateInput) {
  const today = new Date().toISOString().split('T')[0];
  dateInput.min = today;
}

// ---- Welcome strip marquee ----
window.addEventListener('load', function () {
  const track = document.querySelector('.marquee-track');
  if (!track) return;
  const item = track.querySelector('.marquee-item');
  if (!item) return;

  const itemW = item.offsetWidth;
  if (!itemW) return;

  let pos = 0;
  const speed = 0.6; // px per frame (~36 px/s at 60 fps

  function tick() {
    pos -= speed;
    if (pos <= -itemW) pos = 0;
    track.style.transform = 'translateX(' + pos + 'px)';
    requestAnimationFrame(tick);
  }
  requestAnimationFrame(tick);
});

// ---- Hero video mobile autoplay fallback ----
const heroVideo = document.querySelector('.hero-video');
if (heroVideo) {
  const tryPlay = () => heroVideo.play().catch(() => {});
  window.addEventListener('load', tryPlay);
  document.addEventListener('touchstart', tryPlay, { once: true });
}

// ---- Transformation journey — staggered reveal ----
const transformEls = document.querySelectorAll('.transform-card, .transform-connector');

const transformObserver = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const delay = parseInt(entry.target.dataset.delay || 0);
      setTimeout(() => {
        entry.target.classList.add('in-view');
      }, delay);
      transformObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.15, rootMargin: '0px 0px -60px 0px' });

transformEls.forEach(el => transformObserver.observe(el));
