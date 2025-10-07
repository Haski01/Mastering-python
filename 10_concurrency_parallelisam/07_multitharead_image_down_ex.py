import threading
import requests
import time

def download_image(url):
    print(f"Start image downloading from {url}")
    resp = requests.get(url)
    print(f"Finish image downloading from {url}, size: {len(resp.content)} bytes")

urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
]

start = time.time()
threads = []

for url in urls:
   t = threading.Thread(target=download_image, args=(url, ))
   t.start()
   threads.append(t)

[th.join() for th in threads]

end = time.time()
print(f"All images downloaded in {end - start:.2f} seconds")