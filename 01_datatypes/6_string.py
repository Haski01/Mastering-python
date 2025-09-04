#  [What is a String?]

#   - A string is a sequence of characters enclosed in single quotes ('), double quotes ("), or triple quotes (''' / """).
#   - Strings are immutable → once created, they cannot be changed (operations always return a new string).


# [Creating String, Concatination, Format string and Repetation]

# Single and double quotes
s1 = 'Hello'
s2 = "World"

# Triple quotes (for multi-line strings)
s3 = '''This is
a multi-line
string'''

print(s1, s2, s3)

# Concatination and formating string and repetation
print(f"Concatination and string formation: {s1} {s2}")
print(s1 * 3) # HelloHelloHello


# [Accessing Characters]

word = "Python"
print(word[0])   # P → indexing starts at 0
print(word[-1])  # n → negative indexing


# [String Slicing]

text = "Mastering Python"
print(text[0:9])   # 'Mastering' (0 to 8)
print(text[:9])    # 'Mastering' (default start=0)
print(text[10:])   # 'Python'   (from 10 till end)
print(text[-6:])   # 'Python'   (last 6 characters)
print(text[::2])   # skip every second character (from 0 to end)


# [*******************Useful String Methods******************]

# [Case Conversion]

s = "python"
print(s.upper())   # 'PYTHON'
print(s.lower())   # 'python'
print(s.title())   # 'Python'
print(s.capitalize())  # 'Python'


# [Stripping Whitespace]

msg = "   hello   "
print(msg.strip())   # removes both sides → 'hello'
print(msg.lstrip())  # left strip → 'hello   '
print(msg.rstrip())  # right strip → '   hello'


# [Searching & Replacing]

sentence = "I love Python"
print(sentence.find("love"))    # 2 (index)
print(sentence.replace("Python", "Coding"))  # "I love Coding"

# [Checking Content]

word = "Python123"
print(word.isalpha())   # False (contains digits)
print(word.isdigit())   # False (contains letters too)
print("123".isdigit())  # True
print("python".islower()) # True
print("HELLO".isupper()) # True

# [Splitting & Joining]

text = "apple,banana,mango"
fruits = text.split(",")     # ['apple', 'banana', 'mango']
print(fruits)

joined = "-".join(fruits)    # "apple-banana-mango"
print(joined)


# [String Immutability Example]

s = "Hello"
# s[0] = "J"   # ❌ Error: Strings are immutable
s = "J" + s[1:]   # ✅ Correct way
print(s)   # 'Jello'



