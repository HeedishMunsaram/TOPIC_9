num1 = input("Input num1 : ")
num2 = input("Input num2 : ")
operator = input("input operator : ")
if num1.isdigit():
    print("continue")
else:
    num1 = input("Enter a valid number : ")

if num2.isdigit():
    print("continue")
else:
     num2 = input("Enter a valid number : ")

if operator == '+':
    def add(num1, num2):
        num3 = int(num1) + int(num2)
        return num3
    num3 = add(num1, num2)
    print(num3)

if operator == '-':
     def sub(num1, num2):
         num4 = int(num1) - int(num2)
         return num4
     num4 = sub(num1, num2)
     print(num4)

if operator == '*':
    def mul(num1, num2):
        num5 = int(num1) * int(num2)
        return num5
    num5 = mul(num1, num2)
    print(num5)

if operator == '/':
    def div(num1, num2):
        num6 = int(num1) / int(num2)
        return num6
    num6 = div(num1, num2)
    print(num6)

else:
    print("Incorrect Operator")
    operator = input("input operator : ")

    if operator == '+':
        def add(num1, num2):
            num3 = int(num1) + int(num2)
            return num3


        num3 = add(num1, num2)
        print(num3)

    if operator == '-':
        def sub(num1, num2):
            num4 = int(num1) - int(num2)
            return num4


        num4 = sub(num1, num2)
        print(num4)

    if operator == '*':
        def mul(num1, num2):
            num5 = int(num1) * int(num2)
            return num5


        num5 = mul(num1, num2)
        print(num5)

    if operator == '/':
        def div(num1, num2):
            num6 = int(num1) / int(num2)
            return num6


        num6 = div(num1, num2)
        print(num6)