# Nginx Log Analyzer

A service for analyzing Nginx logs and generating statistical reports.

## Features

- Parses Nginx access logs.
- Generates statistical reports including:
  - Total number of requests.
  - Average response time.
  - Median response time.
  - Number of unique IPs.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/speculzzz/nginx-log-analyzer.git
   cd nginx-log-analyzer
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

### Using Uvicorn

To run the application locally, use the following command:
   ```bash
   uvicorn nginx_log_analyzer.main:app
   ```
After running the command, the service will be available at http://127.0.0.1:8000.

### Accessing the Report

Open your browser or use a tool like curl to access the report:

   ```bash
   curl http://127.0.0.1:8000/report
   ```

## Docker

To run the application in a Docker container:

1. Build the Docker image:
   ```bash
   docker build -t nginx-log-analyzer .
   ```
2. Run the container:
   ```bash
   docker run -p 80:80 nginx-log-analyzer
   ```

The service will be available at http://localhost/report.

## Testing
 
Run the tests using pytest:

   ```bash
   pytest
   ```
