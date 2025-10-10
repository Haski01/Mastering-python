- async and await (Asynchronous Programming)

## 🧠 What Is Asynchronous Programming?

- 👉 It means doing multiple tasks “at once”, without blocking each other — but in a single thread.

- It’s different from:

  - Multithreading → runs multiple threads concurrently.
  - Multiprocessing → runs multiple processes in parallel.

- 🌀 Async is about efficient waiting — letting your program do something else while waiting for a slow task (like downloading data, reading files, or network requests).

## ⚡ Real-Life Example

- Imagine you’re a chai seller 🫖

  - You pour one chai and wait for it to boil before serving the next. (That’s synchronous)
  - Or... while the first chai boils, you start preparing another cup — you don’t just stand still. (That’s asynchronous!)

- So, async = “Don’t block while waiting.”

## 🧩 Basic Syntax

- In Python, asynchronous code uses:

  - async def → defines an asynchronous function.
  - await → pauses the function until another async task completes.

- You need an event loop to run async functions — Python provides it using `asyncio`.
