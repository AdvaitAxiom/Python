s = set()
s.add(1)
s.add(1.0)
s.add('1')
s.add('1.0')

print(s)

# In Python, the integer 1 and the float 1.0 are considered equal when it comes to sets and dictionaries because they have the same hash value and are considered equal in terms of their value. Therefore, when you add both 1 and 1.0 to a set, only one of them will be stored, as sets do not allow duplicate values. The string '1' and '1.0' are different from the numeric values, so they will be stored separately in the set.