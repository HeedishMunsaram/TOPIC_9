f = 101;
print(f)
def someFunction():
    global f
    print(f)
    f = 'changing global variable'
someFunction()
print(f)