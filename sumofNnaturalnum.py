num = int(input("Enter a number: "))
result = 0
for i in range (1, num+1):
    result += i

print(f"The sum of first {num} natural numbers is: {result}")