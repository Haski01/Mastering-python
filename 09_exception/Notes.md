## What is an Exception?

- An exception is an error that occurs while the program is running.
- If not handled, it will stop the program.

**Example:-**

```python
num = int("chai")  # ❌ ValueError: invalid literal for int()
```

## Why Exception Handling?

- To prevent the program from crashing.
- To provide meaningful error messages.
- To allow graceful recovery from unexpected situations.

## Common Exceptions

- **ZeroDivisionError** → Dividing by 0
- **ValueError** → Wrong data type conversion
- **FileNotFoundError** → File doesn’t exist
- **TypeError** → Wrong operation on wrong type
- **IndexError** → List index out of range
- **KeyError** → Dictionary key not found
