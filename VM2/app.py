# File: data_service/app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def data():
    sample_data = {"data": [1, 2, 3, 4, 5]}
    return jsonify(sample_data), 200

if __name__ == '__main__':
    # Listen on all interfaces so that the API service on VM1 can connect
    app.run(host='0.0.0.0', port=5002)
