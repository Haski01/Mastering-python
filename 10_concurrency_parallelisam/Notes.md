## 🐍 Concurrency vs Parallelism in Python

### 🔹 Concurrency

- Definition: Doing multiple tasks at the same time in overlapping time frames, but not literally at the same instant.
- Python switches between tasks so it looks like they are running together.
- Best for I/O-bound tasks (waiting on files, network requests).

👉 `Real-life example:` A single waiter serving 3 tables at once. He doesn’t serve them all exactly at the same second, but he switches quickly between them so it feels simultaneous.

### 🔹 Parallelism

- Definition: Doing multiple tasks at the exact same time, usually using multiple CPU cores.
- Best for CPU-bound tasks (heavy computations like math, image processing).

👉 `Real-life example:` 3 waiters serving 3 tables at the same time. Work happens literally in parallel.

#### 📌 Summary

```
- Concurrency = Multiple tasks progressing together (good for waiting tasks).
- Parallelism = Multiple tasks executing at the same instant (good for CPU work).
In Python:
- Use threading / asyncio for concurrency (I/O-bound).
- Use multiprocessing for parallelism (CPU-bound).
```

## 🐍 Multiprocessing vs Multithreading & the GIL

### 🔹 Multithreading

- Definition: Running multiple threads (lightweight tasks) within the same process.
- Threads share the same memory space.
- Best for I/O-bound tasks (waiting for files, network, APIs).
- Example: Multiple chat windows in WhatsApp → All part of the same app, sharing memory but running concurrently.

👉 **In Python**: Done using the `threading` module.

### 🔹 Multiprocessing

- Definition: Running multiple processes in separate memory spaces, often across multiple CPU cores.
- Each process is independent → crash in one process does not affect others.
- Best for CPU-bound tasks (math calculations, image processing, data crunching).
- Example: Running MS Word and Chrome at the same time → They are separate processes, don’t share memory.

👉 **In Python**: Done using the `multiprocessing` module.

## 🔹 The GIL (Global Interpreter Lock)

- Python has something called GIL = Global Interpreter Lock.
- It allows only one thread to execute Python bytecode at a time, even on multi-core CPUs.
- Why? → To protect memory management in Python (since it isn’t thread-safe).

### 👉 Impact:

- For CPU-bound tasks:

  - Multithreading is slowed down by GIL (because only 1 thread can run Python code at a time).
  - Solution → Use multiprocessing (each process has its own Python interpreter & GIL).

- For I/O-bound tasks:

  - GIL is less of a problem since threads often wait for I/O (like file read or network response).
  - Solution → Use multithreading or asyncio.

### 📌 Expected Result

- **Multithreading** → Will be slower for CPU tasks (because of GIL).
- **Multiprocessing** → Faster since both processes run in true parallel on separate cores.

### 🔑 Summary

- Multithreading → Multiple threads, same memory → Best for I/O tasks.
- Multiprocessing → Multiple processes, separate memory → Best for CPU tasks.

- `GIL` → A Python mechanism that prevents multiple threads from running Python bytecode at the same time.
