import math
num = int(input("Enter a number: "))
i = 0
counter = 0

for i in range (2, int(math.sqrt(num))):
    if int(num % i) == 0 or int(num % (num/i)) == 0:
        counter +=1

if counter == 0:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")


for i in range (2, int(math.sqrt(num))):
    if int(num % i) == 0 or int(num % (num/i)) == 0:
        print(f"{num} is not a prime number")
        break
else:
    print(f"{num} is a prime number")
