n = int(input("Enter a number: "))
for i in range (n):
    print(" "*(n-i-1) + "*"*(2*i+1))
    # print("")

for i in range (n):
    print(""*(n-i--1), end="")  #end="" is used to prevent the print function from adding a newline character at the end of the output. By default, the print function adds a newline character after each call, which causes the output to be printed on a new line. By using end="", we can specify that we want to end the output with an empty string instead of a newline, allowing us to continue printing on the same line.
    print("*"*(2*i+1), end="")
    print("")