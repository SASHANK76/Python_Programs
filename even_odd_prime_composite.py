'''
This program helps us to find whether the number is Even , Odd , Prime , Composite
It can choose over a range you have entered
'''
print()
print("Welcome...")
print("1 for checking a number:-")
print("2 for finding in range:-")
a = int(input("Enter choice:-"))

def Even_Odd(n):
    if n % 2 == 0:
        print(n,"Is a Even number..")
    else:
        print(n,"Is a Odd number")

def Prime(n):
    c = 0
    for i in range(1,n+1):
        if n % i == 0:
            c += 1
    if c == 2:
        print(n,"Is a prime number..")
    else:
        print(n,"Is not a prime number")                        

if a == 1:
    num = eval(input("Enter number:-"))
    print("1 for Even-odd")
    print("2 for Prime")
    b = int(input("Enter choice:-"))
    if b == 1:
        Even_Odd(num)
    elif b == 2:
        Prime(num)
elif a == 2:
    x = int(input("Enter starting range:-"))
    y = int(input("Enter ending point:-"))
    print("1 for Even-odd")
    print("2 for Prime")
    b = int(input("Enter choice:-"))
    if b == 1:
        for i in range(x,y+1):
            Even_Odd(i)
        print()
    elif b == 2:
        for i in range(x,y+1):
            Prime(i)
        print()
    else:
        print("Entered number is Invalid..")    

    





