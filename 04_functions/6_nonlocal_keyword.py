#                           [nonlocal keyword]

# Used inside nested functions (a function inside another function).
# It lets the inner function modify variables from the outer (enclosing) function, not the global scope.

chai_type = "ginger"
def update_order():
    chai_type = "Elaichi"
    def kitchen():
        nonlocal chai_type
        chai_type = "Kesar"
    kitchen()
    print("After kitchen update", chai_type)

update_order()
print(f"Outer: {chai_type}")


