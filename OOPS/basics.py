class Employee:
    # name = "Alapan"
    Language = "Python" #class attribute
    Salary = 1200000    #class attribute


Alapan = Employee()
Alapan.name = "Alapan"  #instance attrbute
Alapan.Language = "Cpp" 
print(Alapan.name, Alapan.Language, Alapan.Salary)
# output --> Alapan Cpp 1200000
# Explanation --> instance attribute > classs attribute