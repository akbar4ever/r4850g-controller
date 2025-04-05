#!/bin/bash

echo "🛠️ Menyiapkan lingkungan..."

# Update dan install dependensi
sudo apt update
sudo apt install -y python3 python3-pip python3-flask i2c-tools git
pip3 install flask luma.oled

# Aktifkan I2C jika belum aktif
if ! grep -q "i2c-dev" /etc/modules; then
  echo "i2c-dev" | sudo tee -a /etc/modules
fi

# Tambahkan ke rc.local untuk jalankan OLED saat boot (jika belum)
if ! grep -q "oled_display.py" /etc/rc.local; then
  sudo sed -i '/^exit 0/i python3 /home/orangepi/r4850g-controller/oled_display.py &' /etc/rc.local
fi

# Tambahkan systemd service untuk Web UI
sudo cp systemd/r4850-webui.service /etc/systemd/system/
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable r4850-webui
sudo systemctl start r4850-webui

echo "✅ Instalasi selesai!"