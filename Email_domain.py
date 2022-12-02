print("Welcome...")
a = int(input("Enter number of email you want to enter:-"))
l = []
for i in range(a):
    b = input("Enter Email-id :-")
    l.append(b)
print(l)
for i in l:
    x = i.index('@')
    name = i[0:x]
    domain = i[x+1:]
    print("Username = ",name ," and domain = ",domain)

