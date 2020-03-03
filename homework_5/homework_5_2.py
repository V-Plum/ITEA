try:
    quantity = int(input("How many Febonacci numbers do you want to see? "))
except ValueError:
    print("That's not a number")

# Start
f = [0,1]

# Put n Fibonacci numbers to list
for i in range(1, quantity):
    f_next = f[i] + f[i-1]
    f.append(f_next)

# Print result
print(f[1:quantity])
