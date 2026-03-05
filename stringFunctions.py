#STRING FUNCTIONS

string = "Hakunamatata"
print(string.upper())   #HAKUNAMATATA
print(string.lower())   #hakunamatata
print(string.capitalize())  #Hakunamatata (first letter capitalized)

print(len(string))  #12

print(string.count('A'))    #0 (case-sensitive)
print(string.count('a'))    #5 (case-sensitive)

print(string.endswith('ata'))   #True
print(string.endswith('a'))   #True
print(string.endswith('b'))   #Flase    

print(string.startswith('Haku'))   #True
print(string.startswith('haku'))   #False (case-sensitive)

print(string.find('na'))    #4 (index of the first occurrence of 'na')

str = string.replace('a', 'o')
print(str)    #Hokunomototo (replaces all 'a' with 'o')