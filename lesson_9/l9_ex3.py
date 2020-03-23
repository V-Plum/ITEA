dict1 = {
    1: "one",
    2: "two",
    3: "three",
    4: "three",
    5: "one"
}
result = {}
for word in dict1:
    for key, value in dict1.items():
        if value not in result.values():
            result[key] = value
print(result)