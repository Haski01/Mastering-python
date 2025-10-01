# Exception Handling Syntax

try:
    # Code that may cause error
    x = 10 / 0
except ZeroDivisionError:
    # Handle specific error
    print("❌ Cannot divide by zero!")
finally:
    # Always runs (cleanup code)
    print("✅ This will always run")
