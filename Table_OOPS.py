'''
This program is used to print the table of numbers upto the range provided....
This program coded with OOP's concept..... 
'''

class Table:
    def __init__(self,num):
        self.a = num
    def table(self):
        for i in range(1,(self.a)+1):
            print("Table of",i)
            for j in range(1,11):
                print(i , "*" , j ,"=",i*j)
            print()
num = int(input("Enter the range or last term upto which table will be printed:-"))
x = Table(num)
x.table()                    