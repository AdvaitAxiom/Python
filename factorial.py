num = int(input("Enter a number: "))
result = 1
if num == 0 or num == 1:
    print(f"The factorial of {num} is 1")
else:
    for i in range(num,1,-1):
        result *= i

print(result)
