dict = {
    "Amar" : "My",
    "Naam" : "Name",
    "holo" : "is",
    "Tumi" : "You"
}

word = input("Enter a bengali word: ")

if(word in dict):
    print(dict[word])
else:
    print("Word not found")