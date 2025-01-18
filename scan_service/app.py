from flask import Flask, jsonify
import requests
from aws_services.scanning import scan_s3_file

app = Flask(__name__)

# Buckets and files to scan
buckets = ['bucket1', 'bucket2', 'bucket3']
files = ['All data.txt']

@app.route('/start_scan', methods=['GET'])
def start_scan():
    results = {}

    # Scan each file in each bucket
    for bucket in buckets:
        for file in files:
            matches = scan_s3_file(bucket, file)
            results[f'{bucket}/{file}'] = matches

    # Send scan results to db_service
    try:
        response = requests.post(
            "http://db_service:5002/store_result",  # db_service URL in the Docker network
            json={"matches": results}  # Send matches as JSON
        )
        response_data = response.json()
    except Exception as e:
        return jsonify({"error": f"Failed to send data to db_service: {str(e)}"}), 500

    return jsonify({
        "scan_results": results,
        "db_response": response_data
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
