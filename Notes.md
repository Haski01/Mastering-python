# 🐍 Mastering Python – Getting Started Notes

## 1. Why We Use Python

### ✅ Pros of Python

- `Easy to Learn & Readable` → Clean syntax, close to plain English.
- `Cross-platform` → Runs on Windows, macOS, Linux.
- `Huge Community Support` → Tons of tutorials, libraries, frameworks.
- `Rich Standard Library` → Built-in modules for file handling, math, networking, etc.
- `Versatile` → Used in web dev, AI/ML, data science, automation, game dev, etc.
- `Rapid Development` → Faster to prototype compared to languages like C++/Java.

### ❌ Cons of Python

- `Slower Execution` → Because it’s interpreted (not compiled like C++).
- `High Memory Usage` → Not ideal for memory-constrained devices.
- `Not Native for Mobile Dev` → Rarely used for mobile apps.
- `GIL Limitation` → Global Interpreter Lock affects multi-threading performance.

## 2. Behind the Scenes: How Python Works

- When you run a Python program, here’s what happens step by step:

  - You write Python code in a .py file.
  - Python interpreter reads the code.
  - Code is compiled into Bytecode (.pyc files).
  - The Python Virtual Machine (PVM) executes the bytecode line by line.
  - Output/Result is produced on your screen.

## 3. Setting Up a Virtual Environment in Windows

- A virtual environment is like a separate container for your project. It helps you:
  - Keep dependencies isolated.
  - Avoid conflicts between project libraries.
  - Maintain a clean global Python installation.

1. Create a virtual environment inside your project folder:

```bash
python -m venv env
```

👉`env` is the name of your environment. You can use any name.

2. Activate the environment:

```bash
.\env\Scripts\activate
```

👉 After activation, your terminal will show (env) at the beginning.

3. Deactivate the environment (when done):

```bash
deactivate

```
