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
    url = 'https://<your-website>'
    num_requests = 100  # Number of requests to send
    delay = 0  # Delay between requests in seconds

    requester = AsyncRequester(url, num_requests, delay)
    
    start_time = time.time()
    asyncio.run(requester.run())
    end_time = time.time()
    print(f'Total time taken: {end_time - start_time} seconds')

    requester.generate_report()
    print(f'Complete...')
