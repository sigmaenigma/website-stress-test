# Website Stress Test

This application is designed to stress test a website by sending multiple asynchronous HTTP GET requests and measuring the response times. It uses `aiohttp` for asynchronous HTTP requests and can be run either manually or using Docker.

## Features

- Sends multiple asynchronous HTTP GET requests to a specified URL.
- Measures and reports the response times for each request.
- Generates a summary report with the average response time.

## Requirements

- Python 3.9 or higher
- `aiohttp` library
- Docker if running this using Docker

## Installation

### Docker Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/sigmaenigma/website-stress-test.git
    cd website-stress-test
    ```
2. Build the Docker image:
    ```bash
    docker build -t website-stress-test .
    ```
3. Run the Docker Compose service:
    ```bash
    docker-compose up
    ```

## Configuration

You can configure the application by modifying the following variables in `app.py`:

- `url`: The URL of the website to stress test.
- `num_requests`: The number of requests to send.
- `delay`: The delay between requests in seconds.

### Manual Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/sigmaenigma/website-stress-test.git
    cd website-stress-test
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    python app.py
    ```
    
## Report

After the application completes, it will generate a report with the following information:

- Website URL
- Number of requests sent
- Average response time

### Sample Report
```bash
2024-10-04 14:38:53 --- Report ---
2024-10-04 14:38:53 Website: https://tiempo.llc
2024-10-04 14:38:53 Number of Requests: 100
2024-10-04 14:38:53 Average Response Time: 9.9726 seconds
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```
