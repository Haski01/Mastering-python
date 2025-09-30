# Key Points
"""
    - @property → Turns a method into an attribute-like getter.
    - leaf.age actually calls the age() method, but you don’t need ().
    - @age.setter → Lets you control how a value is set.
    - Example: Here we restrict the valid range of age.
    - Encapsulation → You hide the real variable (_age) and control how it’s read/written 
    - using getter and setter.
"""

class TeaLeaf:
    def __init__(self, age):
        # Private variable (by convention, starts with _)
        self._age = age

    # ✅ Getter method using @property
    @property
    def age(self):
        # Instead of directly returning _age, we add +2
        # So if _age = 2, it shows 4 when accessed
        return self._age + 2
    
    # ✅ Setter method for "age" property
    @age.setter
    def age(self, age):
        # Add validation: age must be between 1 and 5
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Tea leaf age must be between 1 and 5 years")
        

# ----------------- USAGE -----------------

leaf = TeaLeaf(2)

# Calls the @property method (getter)
# Internally runs: leaf.age() but looks like attribute
print(leaf.age)  # Output: 4  (2 + 2)

# Calls the setter method (@age.setter)
leaf.age = 5

# Again calls the getter method
print(leaf.age)  # Output: 7  (5 + 2)
