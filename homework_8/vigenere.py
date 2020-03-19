import string
ukr = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюяАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
char_set = ukr + string.printable
# print(char_set)


def main():
    to_code = input("Enter secret text: ")
    key = input("Enter key: ")
    while len(key) < len(to_code):
        key = key + key
    key = key[:len(to_code)]
    direction = int(input("Do you want to (1) encode or (2) decode?: "))
    if direction == 1:
        print(encode(to_code, key))
    elif direction == 2:
        print(decode(to_code, key))
    else:
        print("oops")


def encode(text, key):
    coded = ""
    for i in range(0, len(text)):
        to_code_sym_index = char_set.find(text[i])
        key_sym_index = char_set.find(key[i])
        char_row = char_set[key_sym_index:] + char_set[:key_sym_index]
        done_sym = char_row[to_code_sym_index]
        coded = coded + done_sym
    return coded


def decode(text, key):
    decoded = ""
    for i in range(0, len(text)):
        key_sym_index = char_set.find(key[i])
        char_row = char_set[key_sym_index:] + char_set[:key_sym_index]
        to_decode_sym_index = char_row.find(text[i])
        done_sym = char_set[to_decode_sym_index]
        decoded = decoded + done_sym
    return decoded


if __name__ == "__main__":
    main()
