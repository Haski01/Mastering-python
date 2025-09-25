# Creates dictionaries in a compact way.


# without dictonary comprehansion
words = ["chai", "latte", "coffee"]
word_length = {}

for item in words:
    word_length[len(item)] = item
# print(word_length)


# with dict comprehension
# exaple1
teas = ["chai", "latte", "coffee"]

word_lengths = {tea: len(tea) for tea in teas}
print(word_lengths)

# exaple2: change inr to usd
tea_prices_inr = {
    "Masala Chai": 40,
    "Green Tea": 50,
    "Lemon Tea": 200
}

tea_prices_usd = {tea: price/80 for tea, price in tea_prices_inr.items()}
print(tea_prices_usd)
