print("WELCOME")
print("Chosse the operation...")
print("1 for addition")
print("2 for division")
print("3 for multiplication")
print("4 for substraction")
a  = int(input("Enter choise:-"))
b = int(input("Enter number of terms in which operation should be done:-"))
l = []
for i in range(b):
    x = eval(input("Enter number:-"))
    l.append(x)
if a == 1:
    ans = sum(l)
    print("Sumation is = ",ans)
elif a == 2:
    c = 1
    for i in range(len(l)):
        c = l[i] / c
    print("Division is =",c)
elif a == 3:
    n = 1
    for i in range(len(l)):
        n = n * l[i]
    print("Multiplication is =",n)
elif a == 4:
    c = 0
    for i in range(len(l)):
        c = l[i] - c
    print("Substraction is =",c)
else:
    print("Entered choise is invalid....")                              