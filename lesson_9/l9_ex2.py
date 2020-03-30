purchases = [
  {
    "name": "banana",
    "price_per_item": 100,
    "quantity": 3
  },
  {
    "name": "apple",
    "price_per_item": 5,
    "quantity": 8
  },
  {
    "name": "ice cream",
    "price_per_item": 150,
    "quantity": 4
  }
]
dict2 = {}
total = 0
for item in purchases:
    total += item["price_per_item"]*item["quantity"]
    dict2[item["name"]] = item["price_per_item"]*item["quantity"]

print("Total:", total)
print(dict2)