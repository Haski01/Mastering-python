# Define a class (blueprint)
class Tea:
    def __init__(self, name, price):   # constructor (called when object created)
        self.name = name              # attribute 1
        self.price = price            # attribute 2

    def describe(self):                # method
        return f"{self.name} costs {self.price} INR"

# Create objects (instances of class)
chai = Tea("Masala Chai", 20)
green = Tea("Green Tea", 25)

# Call method
print(chai.describe())   # Masala Chai costs 20 INR
print(green.describe())  # Green Tea costs 25 INR


