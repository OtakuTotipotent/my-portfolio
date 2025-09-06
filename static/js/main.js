document.addEventListener('DOMContentLoaded', function () {
  const staticPrefixAttr = document.body.getAttribute('data-static-prefix') || '/static/';
  function setBackgrounds() {
    const path = window.location.pathname;
    let videoFile, imageFile;

    const backgroundMap = {
      '/': {
        video: 'videos/world_globe.mp4',
        image: 'images/backgrounds/sky_lab.jpg'
      },
      '/projects/': {
        video: 'videos/live_coding.mp4',
        image: 'images/backgrounds/black_oreo.jpg'
      },
      '/contact/': {
        video: 'videos/moving_man.mp4',
        image: 'images/backgrounds/universe_traveler.jpg'
      },
      '/ordernow/': {
        video: 'videos/power_hands.mp4',
        image: 'images/backgrounds/green_house.jpg'
      },
      // Add more mappings as needed
    };

    // Find the best matching path (prefer the longest matching key)
    let bestKey = '/';
    let selectedBackground = backgroundMap[bestKey];
    for (const [key, value] of Object.entries(backgroundMap)) {
      if (path.startsWith(key) && key.length >= bestKey.length) {
        bestKey = key;
        selectedBackground = value;
      }
    }

    // Set the files
    videoFile = `${staticPrefixAttr}${selectedBackground.video}`;
    imageFile = `${staticPrefixAttr}${selectedBackground.image}`;

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

  // Initialize backgrounds
  setBackgrounds();
  window.addEventListener('pageshow', setBackgrounds);

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