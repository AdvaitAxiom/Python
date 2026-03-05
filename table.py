n = int(input("Enter a number: "))

for i in range (10):
    print(f"{n} x {i+1} = {n*(i+1)}")


word = "hello"
if "h" in word:
    if "e" in word:
        print ("Yes")
    else:
        print("Maybe")
else:
    print("No")