def get_name():
    global name
    name = input("name : ").title()

def get_sname():
    global sname
    sname = input("surname : ").upper()

def get_age():
    global age
    age = input("age : ")

get_name()
get_sname()
get_age()

print("First name :" , name)
print("Surname :" , sname)
print("Age :" , age)
