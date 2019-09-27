def get_animal1():
    global animal1
    animal1 = input("Animal 1 : ").title()

def get_animal2():
    global animal2
    animal2 = input("Animal 2 : ").upper()

def get_animal3():
    global animal3
    animal3 = input("Animal 3 : ").lower()

get_animal1()
get_animal2()
get_animal3()

print("Animal 1 : " , animal1)
print("Animal 2 : " , animal2)
print("Animal 3 : " , animal3)