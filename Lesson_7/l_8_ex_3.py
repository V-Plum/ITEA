def sort_words(sentence):
    words_arr = sentence.split(sep=" ")
    words_arr.sort()
    sorted = " ".join(words_arr)
    return sorted

sentence = input("Enter sentence to sort words: ")
sorted = sort_words(sentence)
print(sorted)
