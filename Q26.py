num1 = input("Input num1 : ")
num2 = input("Input num2 : ")

# Enter whole and even number
def add(num1, num2):
    num3 = int(num1) + int(num2)
    return num3

def sub(num1, num2):
    num4 = int(num1) - int(num2)
    return num4

def mul(num1, num2):
    num5 = int(num1) * int(num2)
    return num5

def div(num1, num2):
    num6 = int(num1) / int(num2)
    return num6

num3 = add(num1, num2)
print(num3)

num4 = sub(num1, num2)
print(num4)

num5 = mul(num1, num2)
print(num5)

num6 = div(num1, num2)
print(num6)