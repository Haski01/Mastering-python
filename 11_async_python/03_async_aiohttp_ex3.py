# 🧠 What This Code Does
"""
This program sends 3 web requests (to the same URL) at the same time — instead of one after another.
It shows how asynchronous I/O (using async + await) can handle many network calls super efficiently.
"""

import asyncio # Python’s built-in library for asynchronous programming.
import aiohttp # A popular async HTTP client — lets you make non-blocking web requests.

# This defines an asynchronous function (also called coroutine).
async def fetch_url(session, url):
    async with session.get(url) as response:
        print(f"Fetch {url} with status {response.status}")

# 👉 What happens here:
"""
- This defines an asynchronous function (coroutine).
- session.get(url) sends a GET request, but doesn’t block your program while waiting for the server.
- The async with ensures the session and request are properly opened and closed.
- When the response arrives, it prints the URL and its HTTP status code (like 200 for OK).
# 💡 Think of it like saying:
- “Start fetching data from the URL, and meanwhile, I’ll handle other requests.”
"""

async def main():
    """
    - We create a list of 3 identical URLs (each one will take about 2 seconds to respond, because of delay/2).
    - So normally, this would take ~6 seconds sequentia
    """
    urls = ["https://httpbin.org/delay/2"] * 3

    """
    - We create a session object that manages all HTTP connections efficiently.
    - This is like opening a single reusable browser window.
    """
    async with aiohttp.ClientSession() as session:

        """
        - Here we create 3 tasks — each calling fetch_url() for one URL.
        - But we don’t await them yet — they are just “scheduled” tasks ready to run.
        """
        tasks = [fetch_url(session,url) for url in urls]
        # tasks = [t1, t2, t3]
        await asyncio.gather(*tasks)

asyncio.run(main())