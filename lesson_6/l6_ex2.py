def summ_digits(y):
    a = 0
    arr = [int(d) for d in str(y)]
    for i in range(0, (len(arr))):
        a += arr[i]
    return(a)


try:
    in_num = int(input("Enter number: "))
except ValueError:
    print("Entered value is not a digit")
while len(str(in_num)) != 1:
    in_num = summ_digits(in_num)
print(in_num)
