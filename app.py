from flask import Flask, render_template, request, jsonify
import json
import threading
import time
import os

app = Flask(__name__)

config_path = 'config.json'
config_lock = threading.Lock()

def load_config():
    with config_lock:
        with open(config_path, 'r') as f:
            return json.load(f)

def save_config(data):
    with config_lock:
        with open(config_path, 'w') as f:
            json.dump(data, f, indent=2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/config', methods=['GET', 'POST'])
def config():
    if request.method == 'POST':
        save_config(request.json)
        return jsonify({'status': 'success'})
    return jsonify(load_config())

@app.route('/api/reset', methods=['POST'])
def reset():
    default = {"voltage": 53.5, "current": 50, "ip_mode": "dhcp"}
    save_config(default)
    os.system("sudo dhclient eth0")
    return jsonify({'status': 'reset'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)