def greet():
    print("Hello")

def greet(name):
    gr = f"Hello, {name}"
    return gr

def greet (name = "Guest"):
    gr = f"Hello, {name}"
    return gr

print(greet())   #Error because the first defination of greet is overwritten by the second one. To fix this we can default parameter value 
print(greet("Alice"))
