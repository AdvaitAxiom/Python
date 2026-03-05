#STRINGS ARE IMMUTABLE
a = "Alapan "
b = 'Das'
c = a+b #Alapan Das
d = '''This is a multi-line string. It can span multiple lines without the need for newline characters.
So write and forgot.'''
e = a*3 #Alapan Alapan Alapan
print(c)    #Alapan Das
print(d)    #This is a multi-line string. It can span multiple lines without the need for newline characters.
print(e)    #Alapan Alapan Alapan

#STRING SLICING [first index : last index] (Last index is exclusive)

sliced = c[0:4]
print(sliced)   #Alap
sliced = c[2:6]
print(sliced)   #apan
sliced = c[-1:-4] 
print(sliced)   #Empty string because the start index is greater than the end index.
sliced = c[-4:-1]
print(sliced)   # Da (with space)

firstCharacter = c[0]
print(firstCharacter)   #A

# c[-4:-1] == c[1:4]
print(c[1:])    #lapan Das (from index 1 to the end of the string)
print(c[:4])    #Alap (from the beginning of the string to index

skipped=c[1:7:2]
print(skipped)  #lpn (from index 1 to 6 with a step of 2)



