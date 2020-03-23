text = input("Enter text: ")
result = 0
substring = ""
for sym in text:
    if sym in substring:
        cut = substring.index(sym)
        substring = substring[cut + 1:] + sym
    else:
        substring += sym
        result = max(result, len(substring))
print(f"Longest substring of entered text with unique symbols is  {result}  symbols long")
