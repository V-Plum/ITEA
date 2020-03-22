import re
text = input("Enter string with text and numbers: ")


def find_numbers(text):
    numbers = re.findall(r'\d+', text)
    print(numbers)


def find_date(text):
    date = re.search(r'(\d+(/|-){1}\d+(/|-){1}\d{2,4})',text).group(1)
    print(date)


def find_words(text):
    words_list = []
    while True:
        word = input("Enter one of words to find in text or hit Enter to continue: ")
        if word:
            words_list.append(word)
            continue
        if not word:
            break
    for word in words_list:
        if re.findall(r"%s" % word, text, re.IGNORECASE):
            print(f"{word} is in text")
        else:
            print(f"{word} is NOT in text")


# find numbers in text
find_numbers(text)

#find dd-mm-yy or dd-mm-yyyy date in text
find_date(text)

# find entered words in text
find_words(text)
