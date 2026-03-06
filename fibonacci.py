ls = []

def fib(n):
    if n ==1:
        ls.append(0)
    elif n ==2:
        ls.append(0)
        ls.append(1)
    else:
        fib(n-1)
        ls.append(ls[-1]+ls[-2])
fib(10)
print(ls)           