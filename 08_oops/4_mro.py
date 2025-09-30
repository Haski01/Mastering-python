# What is MRO?

"""
- MRO = the order in which Python looks for methods/attributes when a class is created.
- Especially important in multiple inheritance.
- Python uses the C3 linearization algorithm to decide the order.
"""

class A:
    def show(self): print("A")

class B(A):
    def show(self):
        super().show()
        print("B")

class C(B):
    def show(self):
        super().show()
        print("C")

c = C()

c.show()
print(C.__mro__)

# Summary for Notes

"""
MRO → Order Python follows to search methods/attributes.
Simple rule: Child → Parent (left to right) → object.
Use super() with MRO for clean multiple inheritance.
Check with ClassName.mro().
"""