s= set()
# s1 = set(1,2,3)
s.add(1)
s.add(3)
s.add(2)
# s.add(3)
print(s)
# print(s1)
print(1 in s)  #returns True if 1 is present in the set, False otherwise
s.remove(2)  #removes 2 from the set 
print(s)
s.discard(3)  #removes 3 from the set, does not raise an error if 3 is not present
print(s)
s.add(4)
s.add(2)
print(s)
print(len(s))  #returns the number of elements in the set
print(s.union({5,6}))  #returns a new set that is the union of s and {5,6}
print(s.intersection({2,4,5}))  #returns a new set that is the intersection of s and {2,4,5}
print(s.difference({2,4,5}))  #returns a new set that is the difference of s and {2,4,5}
# print(s[0]) #sets are unordered, this will raise an error



ex_set = set()
ex_set.add(1)
ex_set.add(3)
ex_set.add(5)
ex_set.add(4)
print(ex_set)


ex_set2 = set()
ex_set2.add(1)
ex_set2.add(1000)
ex_set2.add(50)
ex_set2.add(4100)
print(ex_set2)

# Python sets are implemented using a hash table.
# For small integers:
# The hash of an integer is the integer itself.
# Because of how hashing + memory buckets work,
# Small numbers often appear in sorted-looking order.
# But that is just coincidence, not sorting.


# if set is not ordered then when I take 1,1000,50,4100 then why always it prints in a perticular order of 1000, 1,50, 4100. It should print in different order

# In CPython:

# hash(1)    → 1
# hash(50)   → 50
# hash(1000) → 1000

# For integers (except -1), the hash value is the number itself.

# Python set uses:

# 👉 Open addressing hash table
# 👉 Table size is always a power of 2
# 👉 Bucket index = hash % table_size

# Let’s assume table size = 8 (just for explanation)

# Now compute:

# 1 % 8     = 1
# 1000 % 8  = 0
# 50 % 8    = 2
# 4100 % 8  = 4

# So elements go into buckets:

# Bucket	Value
# 0	1000
# 1	1
# 2	50
# 4	4100

# Now when Python prints a set:

# 👉 It scans buckets from index 0 → end
# 👉 It prints elements in bucket order

# So output becomes:

# {1000, 1, 50, 4100}

# 🔥 That’s why you see a “particular order”.

# It’s bucket order. Not sorted order.

# Why It Looks Same Every Time?

# Because:

# You are running same Python version

# Same hash function

# Same insertion pattern

# Same table resizing behavior

# So buckets are arranged same way → output same.

# ⚠️ But Python does NOT guarantee this behavior.


a = {1,2,3}
b = {4,5,6}
print(a & b | {6})  # a & b means common element between these 2 sets = {} and | union with {6} = {} | {6} = {6}