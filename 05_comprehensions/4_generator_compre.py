# Similar to list comprehension, but uses () instead of [].
# It returns a generator (lazy evaluation — values generated one at a time).

# A generator comprehension is very similar to a list comprehension, but instead of creating the entire list in memory, it creates a generator object that produces items one at a time (lazy evaluation).

# example1
gen = list(i*1 for i in range (1,5+1))
print(gen)

# example2: give the sum of the sales revenue which is more then 5

daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]
total_cups = sum(sale for sale in daily_sales if sale > 5)

print(total_cups)
