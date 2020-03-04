try:
    first_num = int(input("Enter first number of range: "))
    last_num = int(input("Enter second number of range: "))
except ValueError:
    print("Entered value is wrong")

divisors_list = []
num_range = []

for current_num in range(first_num, last_num+1):
    num_range.append(current_num)  # Write numbers to list
    divisors = []  # Reset list with divisors quantity

    # Find number of divisors for c
    for div_try in range(1, current_num+1):
        y = current_num % div_try
        if y == 0:
            divisors.append(y)
        div_quantity = len(divisors)

    divisors_list.append(div_quantity)  # Write quantity of divisors to list

    # Reverse lists to easily find max number with max divisors quantity
    divisors_list.reverse()
    num_range.reverse()
max_index = divisors_list.index(max(divisors_list))  # Find index of first max element

print(f"In range from {first_num} to {last_num} largest number with maximum quantity of divisors is {num_range[max_index]}, with {divisors_list[max_index]} divisors")
