try:
    salary = int(input("Enter your salary: "))
    print("\nWhat is your job?\n1 for Programmer\n2 for Accountant\n3 for Waiter\n4 for Other\n")
    job = int(input("Enter your choice: "))
except ValueError:
    print("\n\x1b[1;31mEntered value is not correct\n")
    exit()

if job == 1:
    tax = round((salary * 0.13), 2)
elif job == 2:
    tax = round((salary * 0.1), 2)
elif job == 3:
    tax = round((salary * 0.07), 2)
elif job == 4:
    tax = round((salary * 0.05), 2)
else:
    print("\n\x1b[1;31mYou entered wrong job code\n")
    exit()

print(f"\n\x1b[1;34mYour tax is {tax}\x1b[0;37m")