# this is not the concept it just the style of writing code
# use dictonary insted of iteration

users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 150, "coupon": "F10"},
    {"id": 3, "total": 80, "coupon": "P50"},
]

discounts = {
    "P20": (0.2, 0),
    "F10": (0.5, 0),
    "P50": (0, 10),
}

for user in users:
    percent, flat = discounts.get(user["coupon"], (0,0)) # (0,0) default val
    discount = user["total"] * percent + flat
    print(f"{user["id"]} paid {user["total"]} and got discount for next visit of rupees {discount}")    