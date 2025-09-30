#               [Inheritance]

"""
    - Child class gets features from Parent class.
    - Relationship: IS-A
"""

class Drink:
    def consume(self):
        return f"This is a drink from parent class"

class Tea(Drink):
    def flavour(self):
        return f"This is a masala tea from child class"

chai = Tea()
print(chai.consume())
print(chai.flavour())

#                            [Composition]

'''
- Instead of inheriting, a class uses another class inside it.
- Relationship: “HAS-A”
'''

class Sugar:
    def add(self):
        print("Adding sugar")

class Tea:
    def __init__(self):
        self.sugar = Sugar()   # Tea HAS-A Sugar

    def prepare(self):
        print("Preparing Tea")
        self.sugar.add()

chai = Tea()
chai.prepare()

