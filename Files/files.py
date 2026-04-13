f= open("file1.txt","r")
data = f.read()
print(data)
f.close()
# if close not used then there can be resource leak or incomplete write or file locking problems.

with open("file1.txt", "r") as f:
    data = f.read()
    print(data)

    # readlines() method reads all the lines of the file and returns a list of strings, where each string is a line from the file. The lines include the newline character at the end of each line.
    line1 = f.readline()
    print(line1)
    line2 = f.readline()
    print(line2)
    line3 = f.readline()
    print(line3)
    line4 = f.readline()
    print(line4)
    line5 = f.readline()
    print(line5)


with open("file1.txt", "w") as f:
    f.write("This is a new line.\n")
    f.write("This is another line.\n") 
    
# replace the content of file1.txt with the above two lines. If you want to append instead of replacing, use "a" mode:

with open("file1.txt", "a") as f:
    f.write("This line will be appended to the file.\n")
    