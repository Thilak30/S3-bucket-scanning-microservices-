from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Fetch database configuration from environment variables
db_config = {
    "host": os.getenv("DB_HOST", "db_service"),  # Adjusted to your environment
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "changeme"),
    "database": os.getenv("DB_NAME", "scan_results"),
    "port": int(os.getenv("DB_PORT", 3306))  # Add port with default 3306
}

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask App!"})

import logging

@app.route('/store_result', methods=['POST'])
def store_result():
    data = request.get_json()
    if not data or 'matches' not in data:
        return jsonify({"error": "Invalid payload"}), 400

    matches = data['matches']  # Extract matches
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Insert scan results into the database
        for bucket_file, results in matches.items():
            for match in results:
                cursor.execute(
                    "INSERT INTO scan_results (bucket_name, `match`) VALUES (%s, %s)",
                    (bucket_file, match)
                )
        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({"message": "Scan results stored successfully!"})

    except Exception as e:
        logging.error("Error occurred while storing results: %s", e)
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
