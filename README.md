# Huawei R4850G Web UI Controller
**By. DMT**

Proyek ini memungkinkan kamu untuk mengatur dan memantau Power Supply Huawei R4850G melalui CAN Bus menggunakan Orange Pi Zero + OLED 0.96" dan Web UI sederhana.

---

## 📦 Fitur

- ✅ Kontrol Voltase & Arus Output R4850G
- ✅ Monitoring Realtime via Web UI (tanpa refresh)
- ✅ Tampilan OLED real-time (voltase, arus, IP, hostname)
- ✅ Web UI aman dengan login (username/password)
- ✅ Konfigurasi IP Static / DHCP langsung dari Web
- ✅ Reset ke konfigurasi default
- ✅ Installer otomatis
- ✅ Ringan & optimal untuk Orange Pi Zero 512MB

---

## 🧰 Perangkat Keras

- Orange Pi Zero (512MB)
- Power Supply Huawei R4850G
- Layar OLED 0.96” I2C (SSD1306)
- CAN Bus Module (MCP2515 via SPI)

---

## ⚙️ Cara Install

1. **Clone repo ini di Orange Pi:**

```bash
git clone https://github.com/akbar4ever/r4850g-controller.git
cd r4850g-controller
```
2. Jalankan installer otomatis:
```bash
chmod +x install.sh
sudo ./install.sh
```
3. Akses Web UI:
Buka browser dan akses:
```bash
http://<IP-OrangePi>:5000

🛡️ Default Login:
Username: admin
Password: admin
```
🖥️ Tampilan OLED
```bash
-------------------------
| Huawei R4850G Monitor |
|                       |
| Set: 53.5V 10.0A      |
| Actual: 53.5V 4.9A    |
|                       |
| Hostname: orangepi    |
| IP: 192.168.1.100     |
-------------------------
```
