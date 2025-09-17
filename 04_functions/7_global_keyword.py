#                           [global keyword]

# Used inside a function when you want to modify a variable defined in the global scope.
# Without global, Python treats assignments inside functions as creating local variables.


# [Example (without global)]
x = 10

def update():
    x = 20   # Creates a LOCAL variable, doesn’t change global x
    print("Inside:", x)

update()
print("Outside:", x)

# Output
# Inside: 20
# Outside: 10



# [Example (with global)]
x = 10

def update():
    global x
    x = 20   # Now modifies GLOBAL x
    print("Inside:", x)

update()
print("Outside:", x)

# Output
# Inside: 20
# Outside: 20
