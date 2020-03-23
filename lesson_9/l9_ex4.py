text = "one two two three three three four four four four five five five five five"
words = text.split(" ")
unique_words = set(words)
counter = {}
num = 0
for i in unique_words:
    if i in words:
        num += 1
        counter[i] = num
print(counter)