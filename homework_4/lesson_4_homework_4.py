try:
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    n3 = int(input("Enter third number: "))
except ValueError:
    print("Entered value is not a number")
    exit()

if n1 <= n2 <= n3:
    print(n1, n2, n3)
elif n1 <= n3 <= n2:
    print(n1, n3, n2)
elif n2 <= n1 <= n3:
    print(n2, n1, n3)
elif n2 <= n3 <= n1:
    print(n2, n3, n1)
elif n3 <= n2 <= n1:
    print(n3, n2, n1)
else:
    print(n3, n1, n2)
