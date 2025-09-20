(function() {
  const btn = document.getElementById('theme-toggle');
  const storageKey = 'site-theme';

  // Function to apply the theme to the HTML element
  function applyTheme(theme) {
    if (theme === 'dark') {
      document.documentElement.classList.add('dark');
      if (btn) btn.textContent = '☀️'; // Sun icon for dark mode
    } else {
      document.documentElement.classList.remove('dark');
      if (btn) btn.textContent = '🌙'; // Moon icon for light mode
    }
  }

  // Set the theme on initial page load without animation
  let savedTheme = localStorage.getItem(storageKey) || 'light';
  applyTheme(savedTheme);

  // Add click listener for the toggle button
  if (btn) {
    btn.addEventListener('click', function() {
      // Toggle the theme
      let newTheme = localStorage.getItem(storageKey) === 'dark' ? 'light' : 'dark';
      applyTheme(newTheme);
      localStorage.setItem(storageKey, newTheme);
    });
  }

  // Enable transitions only after the page has fully loaded
  window.addEventListener('load', () => {
    document.body.classList.add('enable-transitions');
  });
})();