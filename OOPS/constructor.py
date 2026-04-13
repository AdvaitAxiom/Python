class Employee:
    company = 'Concentric AI'
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        print("Employee class constructor called")

Alapan = Employee('Alapan Das', 1200000)
print(Alapan.name, Alapan.salary, Alapan.company)