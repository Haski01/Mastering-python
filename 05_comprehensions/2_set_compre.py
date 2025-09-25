# Similar to list comprehension but creates a set (unique values, unordered).

# example1
nums = [1, 2, 2, 3, 4, 4, 5]

unique_square = {num * num for num in nums}
# print(unique_square)

# example2
favourite_chai = [
    "Masala Chai", "Green Tea", "Masala Chai",
    "Lemon Tea", "Green Tea", "Elaichi Chai"
]

unique_chai = {chai for chai in favourite_chai}
# print(unique_chai)

#example3

recipes = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elaichi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"],
}

unique_spices = {spices for ingredients in recipes.values() for spices in ingredients}

print(unique_spices)

