try:
    amount = float(input("Enter amount: "))
except ValueError:
    print("Entered value is not a number")
    exit()
try:
    in_currency = int(input("What is input currency? Enter 1 for UAH, 2 for USD, 3 for EUR: "))
    if not 1 <= in_currency <= 3:
        raise ValueError("Your choice is not correct")
    out_currency = int(input("What is output currency? Enter 1 for UAH, 2 for USD, 3 for EUR: "))
    if not 1 <= out_currency <= 3:
        raise ValueError("Your choice is not correct")
except ValueError as e:
    print("We can't proceed. ", e)
    exit()

if in_currency == 1 and out_currency == 2:
    result = round((amount / 24),2)
    cur1, cur2 = "UAH", "USD"
elif in_currency == 1 and out_currency == 3:
    result = round((amount / 27),2)
    cur1, cur2 = "UAH", "EUR"
elif in_currency == 2 and out_currency == 1:
    result = round((amount * 24),2)
    cur1, cur2 = "USD", "UAH"
elif in_currency == 2 and out_currency == 3:
    result = round((amount / 1.1),2)
    cur1, cur2 = "USD", "EUR"
elif in_currency == 3 and out_currency == 1:
    result = round((amount * 27),2)
    cur1, cur2 = "EUR", "UAH"
elif in_currency == 3 and out_currency == 2:
    result = round((amount * 1.1),2)
    cur1, cur2 = "EUR", "USD"
else:
    print(f"Nothing to convert, {amount} is {amount}")
    exit()

print(f"\n{amount} {cur1} = {result} {cur2}")
