from functools import wraps

def my_decorator(fun):
    """
    A decorator that adds behavior before and after any function.
    It also supports functions with parameters using *args and **kwargs.
    """
    @wraps(fun)  # ✅ Preserve metadata
    def wrapper(*args, **kwargs):  
        # *args → collects positional arguments
        # **kwargs → collects keyword arguments
        print("Before function run")
        
        result = fun(*args, **kwargs)   # Call original function with arguments
        print("After function run")
        
        return result   # ✅ Return the result of the original function
    return wrapper


# ---------------------------
# Example 1: Function without arguments
# ---------------------------
@my_decorator
def greet():
    print("Hello from decorator")

greet()
print(greet.__name__)   # ✅ "greet"


# ---------------------------
# Example 2: Function with arguments
# ---------------------------
@my_decorator
def greet_person(name):
    print(f"Hello {name}, welcome!")

greet_person("Ad")   # ✅ Passes argument correctly


# ---------------------------
# Example 3: Function with multiple arguments
# ---------------------------
@my_decorator
def add(a, b):
    """Returns sum of two numbers"""
    return a + b

print("Sum:", add(10, 5))  # Works with return value too


# ✅ Key Takeaways

'''
    - *args → packs positional arguments into a tuple
    - **kwargs → packs keyword arguments into a dictionary
    - Always return result if original function returns something.
    - Thanks to @wraps, add.__name__ → "add" (not "wrapper").
'''