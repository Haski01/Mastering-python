# When using inheritance, a child class can access the base (parent) class in different ways.

# Conclusion for Notes
"""
- Version 1 → No parent call → ❌ not recommended.
- Version 2 → Explicit call (Chai.__init__) → ✅ works but less flexible.
- Version 3 → super() → ✅ Best practice in Python.
"""

# [BASE CLASS]
class Chai:
    def __init__(self, type_, strenght):
        self.type = type_
        self.strength = strenght


# Version 1 → Without calling parent constructor

# class GingerChai(Chai):
#     def __init__(self, type_, strength, temperature, spice_level):
#         self.type = type_
#         self.strength = strength
#         self.temperature = temperature
#         self.spice_level = spice_level

"""CodeDuplication
    - Here, Chai.__init__ is not called.
    - You are re-defining parent attributes (type, strength) in child class.
    - Works fine, but not good practice → leads to code duplication.
"""

# Version 2 → Explicit parent call

# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         Chai.__init__(self, type_, strength)   # direct call
#         self.spice_level = spice_level
    
"""Explicit call
- Calls parent constructor directly using class name.
- Ensures type and strength come from parent’s __init__.
- ✅ Better than Version 1 (avoids duplication).
- ❌ But if you change parent class name, you must update it here → less flexible.
"""

class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)   # preferred way
        self.spice_level = spice_level

"""super()
- Calls parent constructor using super().
- ✅ Most recommended way in Python.
- Works with multiple inheritance and respects MRO (Method Resolution Order).
- Clean, flexible, and Pythonic.
"""
        
