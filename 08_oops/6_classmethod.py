# What is a Class Method?
"""
- A method that works with the class itself, not the object.
- First parameter is always cls (refers to the class).
- Defined using @classmethod decorator.
"""

# Class to represent a Chai Order
class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        # Instance variables (unique for each order)
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    # ✅ Class Method - creates object from dictionary
    @classmethod
    def from_dict(cls, order_data):
        # Instead of writing ChaiOrder(...), we use cls(...)
        # This makes the code flexible (works even if class name changes).
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"],
        )
    
    # ✅ Class Method - creates object from string
    @classmethod
    def from_string(cls, order_string):
        # Example input: "Ginger-Low-Small"
        # Split string into 3 parts
        tea_type, sweetness, size = order_string.split("-")
        return cls(tea_type, sweetness, size)
    

# Utility class for helper methods
class ChaiUtils:
    # ✅ Static Method - does not depend on instance or class
    @staticmethod
    def is_valid_size(size):
        # Just checks if given size is valid
        return size in ["Small", "Medium", "Large"]


# -------------------- USAGE ----------------------

# Static method call (No object needed)
print(ChaiUtils.is_valid_size("Medium"))  # ✅ True

# Create ChaiOrder using from_dict (Class Method)
order1 = ChaiOrder.from_dict({"tea_type": "masala", "sweetness": "medium", "size":"Large"})

# Create ChaiOrder using from_string (Class Method)
order2 = ChaiOrder.from_string("Ginger-Low-Small")

# Create ChaiOrder using normal constructor (__init__)
order3 = ChaiOrder("Large", "Low", "Large")

# Print dictionary form of objects (shows instance variables)
print(order1.__dict__)  # {'tea_type': 'masala', 'sweetness': 'medium', 'size': 'Large'}
print(order2.__dict__)  # {'tea_type': 'Ginger', 'sweetness': 'Low', 'size': 'Small'}
print(order3.__dict__)  # {'tea_type': 'Large', 'sweetness': 'Low', 'size': 'Large'}
