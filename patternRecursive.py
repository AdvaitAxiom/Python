'''
*
**
***
****
*****
'''
def pattern(n):
    if n == 0:
        return
    else:
        pattern(n-1)
        print("*"*n)

n = int(input("Enter a number:"))
pattern(n)

'''
*****
****
***
**
*
'''
def pattern(n):
    if n == 0:
        return
    else:
        print("*"*n)
        pattern(n-1)

n = int(input("Enter a number:"))
pattern(n)