friends = ["Alapan", "Rohan", 5, False, 3.14]
print(friends[1])
friends[1]= "Happy"
print(friends[1])   #list are mutable
l1 = [1,2,3,4,1,2,4,5]
print(l1.count(1))  #count the number of times 1 is present in the list
l1.append(6)
print(l1)
l1.insert(2, 100)  #insert 100 at index 2
print(l1)
l1.pop()  #removes the last element
print(l1)
l1.pop(2)  #removes the element at index 2
print(l1)
l1.remove(1)  #removes the first occurrence of 1
print(l1)
l1.reverse()  #reverses the list    
print(l1)
l1.sort()  #sorts the list in ascending order
print(l1)