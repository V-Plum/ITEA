# Get and validate card number
card_number = input("Enter 16 digits of card number: ")
try:
    try:
        card_number_int = int(card_number)
    except ValueError:
        print("Use digits for card number")
        exit()
    if not len(card_number) == 16:
        raise ValueError("Number is not 16 digits long")
except ValueError as e:
    print("Card number is wrong: ", e)
    exit()

# Get and validate expiration date
exp_date = input("Enter card expiration date in MM/YY format: ")
try:
    if not len(exp_date) == 5 and not exp_date.count("/") == 1:
        raise ValueError
    exp_month, exp_year = exp_date.split("/")
    try:
        if not len(exp_month) == 2 or not len(exp_year) == 2:
            raise ValueError("Month and year have to be 2 digits long")
    except ValueError as e:
        print(e)
    exp_month = int(exp_month)
    exp_year = int(exp_year)
    if exp_month < 1 or exp_month > 12:
        raise ValueError("Month have to be in range from 1 to 12.")
except ValueError as e:
    print(e, "Expiration date is wrong. Next time use this mask: MM/YY")
    exit()

# Get and validate CVV number
cvv = input("Enter CVV code: ")
cvv_len = len(cvv)
try:
    cvv_int = int(cvv)
    try:
        if not cvv_len == 3:
            raise ValueError
    except ValueError:
        print("CVV have to be 3 digits long")
        exit()
except ValueError:
    print("CVV should contain only digits")
    exit()

print("Ha-ha-ha. Now I will use your credit card!")
print(f"Number: {card_number}\nExpiration date: {exp_date}\nCVV code: {cvv}")
