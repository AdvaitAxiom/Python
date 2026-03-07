print(10>5 and 3<1)

#output --> True because 10>5 is true and 3<1 is false but since we are using and operator, the overall expression will be false.

for i in range(3):
    if i ==5:
        break
else:
    print("Done")

print(i)

# output -->Prints Done and 2
#  because loop will break when i is 5 but it will never be 5 because loop is running from 0 to 2. So loop will complete and else block will execute and print "Done"(for is executed without any break). After that print(i) will print the last value of i which is 2.

i=1
while i <0:
    print(i)
else:
    print("Done")

# output --> Done because while loop condition is false from the beginning, so loop will not execute and else block will execute and print "Done".