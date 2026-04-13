class calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        return self.num ** 2
    def cube(self):
        return self.num ** 3
    def cuberoot(self):
        return self.num ** (1/3)
    def squareroot(self):
        return self.num ** (1/2)
    
num = int(input("Enter a number: "))
calc = calculator(num)
print(f'square is : {calc.square()}')
print(f'cube is : {calc.cube()}')
print(f'cube root is : {calc.cuberoot()}')
    