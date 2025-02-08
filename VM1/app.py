# File: api_service/app.py
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'API Service is running'}), 200

# Example endpoint to retrieve data from the Data Service on VM2
@app.route('/get-data', methods=['GET'])
def get_data():
    # Replace with the actual internal IP of VM2 if different
    data_service_url = 'http://192.168.56.102:5002/data'
    try:
        response = requests.get(data_service_url)
        return jsonify({
            'message': 'Successfully retrieved data from Data Service',
            'data': response.json()
        }), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Listen on all interfaces so that VM1 can be accessed from VM2 if needed
    app.run(host='0.0.0.0', port=5000)
