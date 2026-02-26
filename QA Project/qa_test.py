import requests
import time

green = '\033[92m'
red = '\033[91m'

url = "https://www.nvidia.com/en-us/"

start = time.time()

print(f"Connecting to {url}...")
response = requests.get(url)

end = time.time()
duration = (end - start) * 1000

print("-" * 34)
if response.status_code == 200:
    print(f"{green}SUCCESS: Server responded in {duration:.2f}ms")
else:
    print(f"{red}FAILURE: Status code {response.status_code}")