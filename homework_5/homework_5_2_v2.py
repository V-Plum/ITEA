try:
    quantity = int(input("How many Fibonacci numbers do you want to see? "))
except ValueError:
    print("That's not a number")
f0 = 0
f1 = 1

# Print first Fibonacci number and calculate next one in a loop "quantity" times
for i in range(0, quantity):
    print(f1)
    f_next = f0 + f1
    f0 = f1
    f1 = f_next
