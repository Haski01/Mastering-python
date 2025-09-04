# An integer (int) is a whole number (positive, negative, or zero).
# No decimal or fractional part.
# Python integers are immutable → changing a value creates a new object in memory.

# ✅ Quick Summary of Integers:

#      - Whole numbers (positive, negative, zero).
#      - Immutable.
#      - Support arithmetic operations.
#      - Can be arbitrarily large.
#      - Useful conversions (bin(), hex(), oct()).
#      - bool is a subclass of int.

# [Creating Integers]

a = 10        # positive integer
b = -50       # negative integer
c = 0         # zero

print(a, b, c)   # Output: 10 -50 0
print(type(a))   # <class 'int'>


# [Integer Immutability]

x = 5
print(id(x))   # memory location of x

x = x + 1      # creates a new integer object
print(id(x))   # different memory location


# [Arithmetic Operations on Integers]

a, b = 10, 3

print(a + b)   # 13 → addition
print(a - b)   # 7  → subtraction
print(a * b)   # 30 → multiplication
print(a / b)   # 3.333... → division (returns float)

print(a // b)  # 3 → floor division (integer result)
print(a % b)   # 1 → modulus (remainder)
print(a ** b)  # 1000 → exponentiation (10^3)


# [******************** Type Convertion and Built-in Integer Functions *******************]

# [Type Conversion]

# int → float
x = 10
print(float(x))   # 10.0

# string → int
num = "123"
print(int(num))   # 123

# binary/hex/oct → int
print(int("1010", 2))  # binary → 10
print(int("A", 16))    # hex → 10
print(int("12", 8))    # octal → 10


# [Built-in Integer Functions]

n = -25

print(abs(n))     # 25 → absolute value
print(pow(2, 3))  # 8  → power function
print(divmod(10, 3))  # (3, 1) → quotient and remainder

print(bin(10))   # '0b1010' → binary representation
print(oct(10))   # '0o12'   → octal representation
print(hex(10))   # '0xa'    → hexadecimal representation


# [Big Integers in Python]
#   - Unlike many languages, Python can handle very large integers.

big_num = 9999999999999999999999999999999999
print(big_num)
print(type(big_num))   # still <class 'int'>


# [Boolean as Subclass of Integer]
#   - In Python, True and False are actually integers (1 and 0).

print(True + 5)   # 6
print(False * 10) # 0
print(isinstance(True, int))   # True
