document.addEventListener('DOMContentLoaded', function () {
  const staticPrefixAttr = document.body.getAttribute('data-static-prefix') || '/static/';
  // Function to set background based on page
  function setBackgrounds() {
    // Get the current page name from the URL or other indicator
    const path = window.location.pathname;
    let videoFile, imageFile;

    // Determine which background to use based on the page
    if (path.includes('work') || path.includes('projects')) {
      videoFile = `${staticPrefixAttr}videos/world_globe.mp4`;
      imageFile = `${staticPrefixAttr}images/backgrounds/black_oreo.jpg`;
    } else if (path.includes('about')) {
      videoFile = `${staticPrefixAttr}videos/moving_man.mp4`;
      imageFile = `${staticPrefixAttr}images/backgrounds/universe_traveler.jpg`;
    } else { // Home page
      videoFile = `${staticPrefixAttr}videos/world_globe.mp4`;
      imageFile = `${staticPrefixAttr}images/backgrounds/sky_lab.jpg`;
    }

    // Set the video background
    const video = document.querySelector('.hero-video');
    const videoSource = document.querySelector('.hero-video source');
    if (video && videoSource) {
      videoSource.src = videoFile;
      video.load();
      video.addEventListener('error', () => {
        const contentSection = document.querySelector('.content-section');
        if (contentSection) {
          contentSection.style.backgroundImage = `url(${imageFile})`;
        }
      }, { once: true });
    }

    // Set the content section background image
    const contentSection = document.querySelector('.content-section');
    if (contentSection) {
      contentSection.style.backgroundImage = `url(${imageFile})`;
    }
  }

  // Intersection Observer for scroll animations
  const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.1
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
      }
    });
  }, observerOptions);

  // Observe elements for animation
  document.querySelectorAll('.hero-content, .fade-in').forEach(el => {
    if (el) {
      observer.observe(el);
    }
  });

  // Header scroll effect
  let lastScrollY = window.scrollY;
  const header = document.querySelector('header');

  window.addEventListener('scroll', () => {
    if (!header) return;

    if (window.scrollY > lastScrollY && window.scrollY > 200) {
      header.style.transform = 'translateX(-50%) translateY(-100px)';
    } else {
      header.style.transform = 'translateX(-50%) translateY(0)';
    }
    lastScrollY = window.scrollY;

    // Add blur effect when scrolled
    if (window.scrollY > 50) {
      header.style.backdropFilter = 'blur(15px)';
      header.style.webkitBackdropFilter = 'blur(15px)';
      header.style.background = 'rgba(255, 255, 255, 0.08)';
    } else {
      header.style.backdropFilter = 'blur(10px)';
      header.style.webkitBackdropFilter = 'blur(10px)';
      header.style.background = 'rgba(255, 255, 255, 0.1)';
    }
  });

  // Initialize backgrounds
  setBackgrounds();

  // Make hero content visible after a short delay
  const heroContent = document.querySelector('.hero-content');
  if (heroContent) {
    setTimeout(() => {
      heroContent.classList.add('visible');
    }, 300);
  }
  // Mobile menu toggle
  const menuToggle = document.getElementById('menuToggle');
  const primaryNav = document.getElementById('primaryNav');
  if (menuToggle && primaryNav) {
    menuToggle.addEventListener('click', () => {
      const isOpen = primaryNav.classList.toggle('open');
      menuToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
  }

  // Active nav link highlight
  const currentPath = window.location.pathname.replace(/\/$/, '');
  document.querySelectorAll('#primaryNav .btn-link').forEach(link => {
    const href = link.getAttribute('href') || '';
    const normalized = href.replace(/\/$/, '');
    if (normalized === currentPath || (currentPath === '' && normalized === '/')) {
      link.classList.add('active');
    }
  });
});