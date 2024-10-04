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
### Script Details

```py
import aiohttp
import asyncio
import time

class AsyncRequester:
    def __init__(self, url, num_requests, delay):
        self.url = url
        self.num_requests = num_requests
        self.delay = delay
        self.response_times = []

    async def fetch(self, session, i):
        try:
            start_time = time.time()
            async with session.get(self.url) as response:
                end_time = time.time()
                response_time = end_time - start_time
                self.response_times.append(response_time)
                print(f'Request {i+1}: Status Code: {response.status}, Response Time: {response_time} seconds')
        except aiohttp.ClientError as e:
            print(f'Request {i+1}: Error: {e}')

    async def run(self):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for i in range(self.num_requests):
                tasks.append(self.fetch(session, i))
                await asyncio.sleep(self.delay)
            await asyncio.gather(*tasks)

    def generate_report(self):
        total_requests = len(self.response_times)
        average_response_time = sum(self.response_times) / total_requests if total_requests > 0 else 0
        print("\n--- Report ---")
        print(f"Website: {self.url}")
        print(f"Number of Requests: {total_requests}")
        print(f"Average Response Time: {average_response_time:.4f} seconds")

if __name__ == "__main__":
    print(f'Running... ')
    url = 'https://tiempo.llc'
    num_requests = 100  # Number of requests to send
    delay = 0  # Delay between requests in seconds

    requester = AsyncRequester(url, num_requests, delay)
    
    start_time = time.time()
    asyncio.run(requester.run())
    end_time = time.time()
    print(f'Total time taken: {end_time - start_time} seconds')

    requester.generate_report()
    print(f'Complete...')
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```
