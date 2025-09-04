# [***************Encoding & Decoding in Strings****************]


# 1. What is Encoding?

#   - Encoding means converting a string (human-readable text) into bytes (machine-readable format).
#   - Useful when saving text to files, sending data over a network, or handling different languages.


# [Encoding example]

text = "Hello, Asad!"

# Encoding string into bytes (UTF-8 is default)
encoded_text = text.encode("utf-8")
print(encoded_text)     # b'Hello, Asad!'
print(type(encoded_text))  # <class 'bytes'>




# 2. What is Decoding?
#   - Decoding is the reverse: converting bytes back into a string.

# [Decoding Example]

# Decoding back into string
decoded_text = encoded_text.decode("utf-8")
print(decoded_text)     # Hello, Asad!
print(type(decoded_text))  # <class 'str'>


# [***************** Encoding types ***********************]

# UTF-8 → Most common, supports all Unicode characters, backward compatible with ASCII.
# ASCII → Only supports English letters, numbers, and symbols.
# UTF-16/UTF-32 → Wider Unicode support but uses more bytes.

text = "Python 🐍"

utf8_encoded = text.encode("utf-8")
utf16_encoded = text.encode("utf-16")

print(utf8_encoded)   # UTF-8 → b'Python \xf0\x9f\x90\x8d'
print(utf16_encoded)  # UTF-16 → b'\xff\xfeP\x00y\x00t\x00h\x00o\x00n\x00 ...'



