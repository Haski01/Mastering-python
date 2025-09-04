# A float represents real numbers (numbers with a decimal point).
# Can also be written in scientific notation (e or E).
# Floats are immutable.

# [Example]

x = 10.5       # float number
y = -3.14      # negative float
z = 2.5e3      # scientific notation → 2.5 × 10³ = 2500.0

print(x, y, z)
print(type(x))   # <class 'float'>



# [****************Decimal & Fraction datatype***************** ]


# [Floating Point Precision Problem]
#   - Floats in Python are based on binary floating-point arithmetic, which may cause rounding issues.

print(0.1 + 0.2)   # 0.30000000000000004 ❌


#  [ Decimal Datatype (decimal.Decimal) ******************]

# What is Decimal?

#   - Comes from the decimal module.
#   - Provides high precision arithmetic (avoids float rounding errors).
#   - Useful in finance, currency, and scientific calculations.

from decimal import Decimal, getcontext

# setting precision
getcontext().prec = 2   # upto 2 value after point

a = Decimal('0.1')
b = Decimal('0.2')
print(a + b)   # 0.3 (exact result ✅)

# high precision example
c = Decimal('1') / Decimal('7')
print(c)   # 0.14286 (5 digits precision)

#   - ✔ Always pass strings to Decimal, not floats (to avoid inheriting float errors).



#  [Fraction Datatype (fractions.Fraction) ******************************]

#   - What is Fraction?

#   - Comes from the fractions module.
#   - Represents numbers as rational fractions (numerator/denominator).
#   - Gives exact results where floats fail.

from fractions import Fraction

# Fraction(Numinator,Denominator)
f1 = Fraction(1, 3) # convert it into 1/3
f2 = Fraction(2, 5)

print(f1 + f2)     # 1/3 + 2/5
print(f1 * f2)     # 1/3 * 2/5

# converting float → fraction
print(Fraction(0.5))      # 1/2
print(Fraction("0.1"))    # 1/10


# [*********************** BONUS ***********************]

# When to Use Float, Decimal, and Fraction?
#     - Float : General calculations, scientific computing, fast operations.
#     - Decimal : Financial & monetary calculations where precision is critical.
#     - Fraction : Exact rational arithmetic (fractions, ratios, probability).



# [Quick Example (Comparison)]

# Float problem
print(0.1 + 0.2)   # 0.30000000000000004 ❌

# Decimal fixes it
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2'))  # 0.3 ✅

# Fraction keeps exact rational value
from fractions import Fraction
print(Fraction(1, 10) + Fraction(2, 10))  # 3/10 ✅




# ✅ Quick Summary:

#       - Float: Fast but has precision issues.
#       - Decimal: High precision, best for finance.
#       - Fraction: Exact rational numbers, best for fractions/ratios.