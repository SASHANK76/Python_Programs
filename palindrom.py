'''
This program helps us to find whether a number is palindrom or not.
It can do another thing , instead of checking you can provide a range and i can automatically give you the palindrom number
present in that range..
'''

print("Welcome..")
print("1 for checking palindrom number:-")
print("2 for getting palindrom number from the entered range")
a1 = int(input("Enter choice:-"))
if a1 == 1:
    x = input("Enter number:-")
    y = x[::-1]
    if x == y:
        print(x,"Is a palindrom number......")
    else:
        print(x,"Is not a palindrom number...") 
elif a1 == 2:
    x = int(input("Enter starting number or point:-"))
    y = int(input("Enter last point:-"))
    for i in range(x,y+1):
        m = str(i)
        n = m[::-1]
        if m == n:
            print(i,"Is a palindrom number")
        else:
            continue
else:
    print("Entered choice is invalid.....")                        