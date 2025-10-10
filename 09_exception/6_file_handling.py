# Without 'with' (requires manual closing)

# file = open("example.txt", "w")
# try:
#     file.write("Hello, world!")
# finally:
#     file.close()

# With 'with' (automatic closing)
with open("example.txt", "w") as file:
    file.write("Hello, world!")
    
"""
In the with example, the open() function returns a file object that is a context manager. When the with block is entered, the file is opened. When the block is exited (either normally or due to an error), the __exit__ method of the file object is called, automatically closing the file.
"""