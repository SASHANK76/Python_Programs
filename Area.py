'''
This program is used to for finding the area of certain shapes.
LIKE:-
1 } Circle
2 } Triangle
3 } Rectangle
4 } Square
5 } Cylinder
6 } Cone
'''
import math
print()
print("Welcome..")
print("1 for Triangle")
print("2 for circle")
print("3 for Rectangle")
print("4 for Square")
print("5 for cone")
print("6 for Cylinder")
a = int(input("Enter choice:-" ))
def Triangle(b,h):
    x = (b * h * (0.5))
    print("Area of Triangle is",x)
def Circle(r):
    x =   math.pi * pow(r,2)
    print("Area of Circle is",x)
def Rectangle(l,b):
    x = l * b
    print("Area of Rectangle is",x)
def Square(l):
    print("Area of Square is",l*l)
def Cone(r,h):
    x = (math.pi * pow(r,2) * h) / 3
    print("Area of Cone is",x)
def Cylinder(r,h):
    x = math.pi * pow(r,2) * h
    print("Area of Cylinder is",x)
if a == 1:
    b = eval(input("Enter base:-"))
    h = eval(input("Ener height:-"))
    Triangle(b,h)
elif a ==2:
    r = eval(input("Enter radius:-"))
    Circle(r)
elif a ==3:
    l = eval(input("Enter length:-"))
    b = eval(input("Enter bredth:-")) 
    Rectangle(l,b) 
elif a == 4:
    s = eval(input("Enter side of square:-"))
    Square(s)
elif a ==5:
    r = eval(input("Enter radius:-"))
    h = eval(input("Enter height:-"))
    Cone(r,h)
elif a ==6:
    r = eval(input("Enter radius:-"))
    h = eval(input("Enter height:-"))
    Cylinder(r,h)
else:
    print("Entered chioce is invalid")                                          