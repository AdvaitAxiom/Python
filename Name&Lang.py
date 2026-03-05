s = {}

for i in range(4):
    print("Enter name and language:")
    name = input("Name: ")
    language = input("Language: ")
    s.update({name: language})

print(s)

#key should not be same
