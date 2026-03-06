num = int(input("Enter a number:"))

for i in range(num):
    if(i == 0 or i == num-1):
        print("*"*num)
    else:
        print("*"+" "*(num-2)+"*")

