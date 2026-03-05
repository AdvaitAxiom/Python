a = (1,2,'Alapan', 3.14, False)
b= ()
print(a)
print(type(a))
c = (1,)  #tuple with one element, need to add a comma
print(c)
# a[0] = 100  #tuples are immutable, this will raise an error
print(a.index(3.14))  #returns the index of the first occurrence of 3.14
print(a.count(1))  #returns the number of times 1 is present in the tuple
print(2 in a)  #returns True if 2 is present in the tuple, False otherwise
print(len(a))  #returns the number of elements in the tuple
sliced = a[1:4]  #slices the tuple from index 1 to 3 (4 is exclusive)
print(sliced)