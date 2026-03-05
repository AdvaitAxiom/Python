names = ["Alice", "Bob", "Charlie", "David"]
name = input("Enter your name:")
# for name in names:
if name in names:
    print(f"Hello, {name}")
else:
    print("Who are you?")

for n in names:
    if (n.startswith("A")):
        print(f"Hello, {n}")

a = 5
b = 2
print(a>b and b>1)  # True and True → True