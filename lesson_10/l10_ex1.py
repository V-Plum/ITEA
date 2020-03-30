def symbols_add(f):
    def wrapped(text):
        if text[1] != '"':
            text = '"' + text
        if text.strip()[-1] != '"':
            text = text + '"'
        return text


@symbols_add
def text_input():
    text = input("Print some text: ")
    return text


def main():
    text = text_input()
    print(text)


if __name__ == '__main__':
    main()
