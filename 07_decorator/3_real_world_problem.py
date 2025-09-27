from functools import wraps   # keeps the original function's metadata

# Step 1: Define the decorator
def require_admin(func):
    @wraps(func)   # ensures func.__name__, docstring aren’t lost
    def wrapper(user_role):   # the wrapper accepts a 'user_role'
        
        # Step 2: Check condition
        if user_role != "admin":  
            print("Access denied: Admins only")   # not allowed
            return None  
        else:
            return func(user_role)  # if admin → run the original function
    
    return wrapper   # return the wrapped function

# Step 3: Apply the decorator
@require_admin
def acess_tea_inventory(role):
    print("Access granted to tea inventory")

# Step 4: Test the function
acess_tea_inventory("user")   # user is not admin → denied
acess_tea_inventory("admin")  # role is admin → granted
