'''This program helps us to check whether the entered number is ARrmstrong or not
Armstrong means:-
let a = 153
if 1^3 + 5^3 + 3^3 == a == 153 . Then it's Armstrong number.........
'''

print("Welcome")
a = input("Enter number to be checked as Armstrong:-")
b = len(a)
l = []
for i in range(b):
    c = int(a[i]) ** b
    l.append(c)
x = sum(l)
if x == int(a):
    print(int(a),"Number is Armstrong")
else:
    print(int(a),"Number is not Armstrong")        