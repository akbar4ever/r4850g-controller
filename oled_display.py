from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from PIL import Image, ImageDraw, ImageFont
import json
import time
import socket

CONFIG_PATH = "config.json"

def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "N/A"

def get_hostname():
    return socket.gethostname()

def load_config():
    with open(CONFIG_PATH, "r") as f:
        return json.load(f)

serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)

font = ImageFont.load_default()

while True:
    config = load_config()
    voltage_set = config.get("voltage", 0)
    current_set = config.get("current", 0)

    actual_voltage = 53.5  # Dummy value; update from CAN bus
    actual_current = 4.9   # Dummy value; update from CAN bus

    image = Image.new("1", (device.width, device.height))
    draw = ImageDraw.Draw(image)

    draw.text((0, 0), "Huawei R4850G Monitor", font=font, fill=255)
    draw.text((0, 12), f"Set: {voltage_set:.1f}V {current_set:.1f}A", font=font, fill=255)
    draw.text((0, 22), f"Actual: {actual_voltage:.1f}V {actual_current:.1f}A", font=font, fill=255)
    draw.text((0, 36), f"Hostname: {get_hostname()}", font=font, fill=255)
    draw.text((0, 46), f"IP: {get_ip()}", font=font, fill=255)

    device.display(image)
    time.sleep(2)