(function(){
  const btn = document.getElementById('theme-toggle');
  const storageKey = 'site-theme';
  function applyTheme(theme) {
    if (theme === 'dark') {
      document.documentElement.classList.add('dark'); if (btn) btn.textContent = '☀️';
    } else {
      document.documentElement.classList.remove('dark'); if (btn) btn.textContent = '🌙';
    }
  }
  let theme = localStorage.getItem(storageKey);
  if (!theme) { theme = 'light'; localStorage.setItem(storageKey, theme); }
  applyTheme(theme);
  if (btn) btn.addEventListener('click', function(){
    theme = localStorage.getItem(storageKey) === 'dark' ? 'light' : 'dark';
    localStorage.setItem(storageKey, theme);
    applyTheme(theme);
  });
})();
