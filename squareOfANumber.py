a = int (input("Enter a number: "))
c = a*a
print(c)
print("The square of " + str(a)+ " is: "+ str(a*a))
print("The square of " + str(a)+ " is: "+ c)
#Here typecasting the result is important to concatinate with the string. Otherwise, it will throw an error.