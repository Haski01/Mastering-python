# What is a Static Method?
"""
- A method inside a class that does not depend on the object (self) or the class (cls).
- Works like a normal function, but is grouped inside a class for better organization.
- Defined using @staticmethod decorator.
"""

class ChaiUtils:
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]
    

raw = " water , milk , ginger , honey "

# Call without creating object
cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)

# Or call from object
chai_object = ChaiUtils()
cleaned_chai = chai_object.clean_ingredients(raw) 
print(cleaned)
