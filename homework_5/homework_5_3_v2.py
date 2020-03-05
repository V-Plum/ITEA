try:
    first_num = int(input("Enter first number of range: "))
    last_num = int(input("Enter second number of range: "))
except ValueError:
    print("Entered value is wrong")

max_divisor = 0

for current_num in range(first_num, last_num+1):
    current_div = 0  # Reset list with divisors quantity

    # Find number of divisors for c
    for div_try in range(1, current_num+1):
        y = current_num % div_try
        if y == 0:
            current_div += 1
    if current_div >= max_divisor:
        max_divisor = current_div
        max_num = current_num

print(f"In range from {first_num} to {last_num} largest number with maximum quantity of divisors is {max_num}, with {max_divisor} divisors")
