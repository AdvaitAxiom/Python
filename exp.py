string = "Pizza"
string.replace("z", "s")   #This does not change the original string because strings are immutable.
print(string)    #Pizza


word = "Python"
word1 = word.replace("P", "J")   #This creates a new string and assigns it to the variable 'word'.

print(word, word1)