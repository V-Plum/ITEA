def main():
    text = input("Enter text: ")
    rows = int(input("Enter number of ZigZag rows: "))
    new_text = string_to_zigzag(text, rows)
    print("New text is", new_text)


def string_to_zigzag(text, rows):
    if rows == 1:
        return text
    list(text)
    matrix = {}
    for i in range(rows):
        matrix[i] = []
    row = 0
    for symbol in range(len(text)):
        if row == 0:
            direction = "down"
        elif row == rows-1:
            direction = "up"
        matrix[row].append(text[symbol])
        if direction == "up":
            row -= 1
        else:
            row += 1
    for i in range(rows):
        matrix[i] = "".join(matrix[i])
    new_string = "".join(map(str, matrix.values()))
    return new_string


if __name__ == '__main__':
    main()
