file = open("lorem", "r+")
while True:
    line = file.readlines(1)
    if line == "":
        False
    for words in line:
        word = words.split(" ")
        print(word, len(word))