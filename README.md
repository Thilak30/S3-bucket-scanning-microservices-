# S3-bucket-scanning-microservices-
Microservices project for scanning AWS S3 buckets, identifying sensitive data, and storing results in a MySQL database. Includes Flask-based APIs, Dockerized services, and a scalable architecture for efficient data processing

The project consists of three main microservices:

UI Service: Provides a user interface to initiate scans and view results. It communicates with the scan service to trigger scanning processes.

Scan Service: Handles the scanning of S3 buckets for sensitive data. It processes bucket contents, identifies matches, and sends results to the database service.

Database Service: Manages the storage and retrieval of scan results using MySQL. It ensures efficient data handling and integrates with the scan and UI services for seamless communication.
