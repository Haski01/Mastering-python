# #                   [Walrus Operator (:=) in Python]

# # 1. What is it?

# #   - It’s called the “assignment expression operator”.
# #   - It lets you assign a value to a variable as part of an expression.
# #   - Before Python 3.8 → you had to separate assignment and usage into two lines.
# #   - With := → you can do both in one line.


# value = 13

# if remainder:= value % 5:
#     print(f"{value} Not devisible by 5: Remainder -> {remainder}")


# available_sizes = ["small", "medium", "large"]

# if (size := input("Enter chai size: ")) in available_sizes:
#     print(f"Serving {size} chai")
# else:
#     print("Size not available")



# flavors = ["masala", "ginger", "lemon", "mint"]

# print("Available flavors: ", flavors)

# while (flavor := input("Choose your flavor: ")) not in flavors:
#     print(f"Sorry, {flavor} is not available")

# print(f"You choose {flavor} chai")


while (name := input("Enter your name: ")) != "quite":
    print(f"Your name is {name}")