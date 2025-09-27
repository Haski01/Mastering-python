from functools import wraps   # ✅ Import wraps to preserve function metadata (like name, docstring)

# ---------------------------
# Step 1: Define a decorator
# ---------------------------
def my_decorator(fun):
    """
    my_decorator takes a function (fun) as an argument
    and returns a new function (wrapper) that adds extra behavior.
    """
    
    @wraps(fun)  # ✅ Ensures metadata of 'fun' is not lost when wrapped
    def wrapper():
        print("Before function run")   # Extra behavior (runs before the actual function)
        fun()                          # Call the original function
        print("After function run")    # Extra behavior (runs after the actual function)

    return wrapper   # ✅ Return the wrapper (not executed yet)


# ---------------------------
# Step 2: Use the decorator
# ---------------------------
@my_decorator     # Same as: greet = my_decorator(greet)
def greet():
    """This function just prints a greeting message"""
    print("Hello from decorator")


# ---------------------------
# Step 3: Call the decorated function
# ---------------------------
greet()
# When greet() is called:
# 1. Control goes to wrapper()
# 2. "Before function run" prints
# 3. greet() (original function) prints "Hello from decorator"
# 4. "After function run" prints

# ---------------------------
# Step 4: Check function metadata
# ---------------------------
print(greet.__name__)   # ✅ Because of @wraps, this will print "greet" (not "wrapper")


#                           [ Important notes ]
'''
# ✅ Why @wraps is important?
    - Without @wraps(fun), Python would think the decorated function’s name is "wrapper" instead of "greet".
'''
print(greet.__name__)  # Without wraps → wrapper
print(greet.__name__)  # With wraps → greet ✅


# ⚡ Quick Reminder in Your Own Words:
'''
    - Decorator = function that wraps another function.
    - @wraps = keeps the original function’s identity (so debugging & docs don’t get messed up).
    - @decorator = shorthand for func = decorator(func).
'''