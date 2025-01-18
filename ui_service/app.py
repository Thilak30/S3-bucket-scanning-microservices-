from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

scan_service_url = "http://scan_service:5001/start_scan"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_scan')
def start_scan():
    response = requests.get(scan_service_url)
    scan_results = response.json()
    return render_template('index.html', results=scan_results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
