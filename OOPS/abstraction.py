class Employee:
    a = 1
    @classmethod
    def classM(cls):
        print(cls.a)
    @property
    def name(self):
        return self.fname, self.lname
    @name.setter
    def name(self, name):
        self.fname = name.split(" ")[0]
        self.lname = name.split(" ")[1]

Alapan = Employee()
Alapan.name = "Alapan Das"

print(Alapan.name)
print(Alapan.fname)
print(Alapan.lname)

Alapan.a = 10
Alapan.classM()