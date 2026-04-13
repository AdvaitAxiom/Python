class Employee:
    lang = 'Python'
    def getInfo(self):
        print(f'language is {self.lang}')
    @staticmethod
    def greet():
        print("Hello")
    
    def __init__(self): #dunder method or magic method or constructor
        print("Employee class constructor called")

Alapan = Employee()     #instance of class Employee
Alapan.name = "Alapan Das"

print(Alapan.name, Alapan.lang)
print(Alapan.getInfo()) #Employee.getInfo() takes 0 positional arguments but 1 was given without self parameter. This is because when we call getInfo() method using the instance Alapan, it automatically passes the instance as the first argument to the method. So, we need to define the method with self parameter to accept that instance.
print(Employee.greet()) #Hello because greet() is a static method and it can be called using the class name without creating an instance of the class.
print(Alapan.greet()) #Hello because greet() is a static method and it can be called using the instance of the class as well.