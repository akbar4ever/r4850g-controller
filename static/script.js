function loadConfig() {
  fetch('/api/config')
    .then(res => res.json())
    .then(data => {
      document.getElementById('voltage').value = data.voltage;
      document.getElementById('current').value = data.current;
      document.getElementById('ip_mode').value = data.ip_mode;
    });
}

function saveConfig() {
  const voltage = parseFloat(document.getElementById('voltage').value);
  const current = parseFloat(document.getElementById('current').value);
  const ip_mode = document.getElementById('ip_mode').value;

  fetch('/api/config', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ voltage, current, ip_mode })
  }).then(() => alert('✅ Konfigurasi disimpan!'));
}

function confirmReset() {
  document.getElementById('popup').classList.remove('hidden');
}

function resetConfig() {
  fetch('/api/reset', {
    method: 'POST'
  }).then(() => {
    alert('🔄 Direset ke default!');
    closePopup();
    loadConfig();
  });
}

function closePopup() {
  document.getElementById('popup').classList.add('hidden');
}

window.addEventListener('focus', loadConfig);
window.onload = loadConfig;