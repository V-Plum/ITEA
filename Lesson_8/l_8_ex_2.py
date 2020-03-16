a = input("str 1: ")
b = input("str 2: ")
a1, b1 = "", ""
for i in a:
    if i.isdigit():
        a1 += i

for i in b:
    if i.isdigit():
        b1 += i

if int(a1) == int(b1):
    print("equal")
else:
    print("not equal")
