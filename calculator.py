class calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return num1 + num2

    def subtract(self):
        return num1 - num2

    def multiplication(self):
        return num1 * num2

    def division(self):
        return num1 / num2

    def modulo(self):
        return num1 % num2

    def res(self):
        print("result is:", self.add, self.subtract, self.multiplication, self.division, self.modulo)


while True:
    ip = input("enter the expression:")
    var = ip.split(" ")
    num1 = float(var[0])
    num2 = float(var[2])
    op = var[1]
    obj = calculator(num1, num2)
    if op == '+':
        print(obj.add())
    elif op == '-':
        print(obj.subtract())
    elif op == '*':
        print(obj.multiplication())
    elif op == '/':
        try:
            print(obj.division())
        except:
            print("Its not possible..!")
    elif op == '%':
        print(obj.modulo())
    else:
        print("enter the valid input")
