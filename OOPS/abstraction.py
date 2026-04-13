class Employee:
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