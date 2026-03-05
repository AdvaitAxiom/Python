ls= [1,2,"Alapan", False, 3.14, 5,6,7,8,9,10]

i = 0
while i <len(ls):
    print(ls[i])
    i+=1

print()

j = 0
for j in ls:    #like for-each loop
    print(j) 

print()

i = 0 
for i in range(2,5):
    print(ls[i])

print()

i = 0 
for i in range(1,9,2):
    print(ls[i])  
else: 
    print("Loop is over")

print()

for i in range(10):
    # print(i)    #prints from 0 to 5
    if i == 5: 
        break  #exits the loop when i is 5
    print(i)    #prints form 0 to 4

print()

for i in range(10):
    if i == 5: 
        continue  #skips the rest of the loop when i is 5 and continues with the next iteration
    print(i)    #prints from 0 to 9 except 5

print()

for i in range(10):
    if i == 5: 
        pass    #do nothing when i is 5, just a placeholder for future code
    print(i)