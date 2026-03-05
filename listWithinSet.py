s = {8,7,12,"hello",[1,2]}  # This will raise a TypeError because lists are mutable and cannot be added to a set. Sets can only contain immutable (hashable) types, such as integers, floats, strings, and tuples. To fix this, you can use a tuple instead of a list:
print(s)
