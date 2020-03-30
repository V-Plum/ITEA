def num_to_roman(num):
    roman = ''
    roman_values = {
        1000: "M",
        500: "D",
        100: "C",
        50: "L",
        10: "X",
        9: "IX",
        8: "IIX",
        5: "V",
        4: "IV",
        1: "I"
    }
    for key in roman_values:
        while num >= key:
            roman += roman_values[key]
            num -= key
    return roman


def main():
    try:
        int_num = int(input("Enter positive integer number to convert to roman numeral: "))
        if int_num < 0:
            raise ValueError
    except ValueError:
        print("Entered value is not positive integer number")
        exit()
    if int_num == 0:
        print("According to Wikipedia, the number zero does not have its own Roman numeral,")
        print("but the word 'nulla' (the Latin word meaning 'none') was used by medieval scholars in lieu of 0")
        exit()
    roman = num_to_roman(int_num)
    print(f"Roman numeral for {int_num} is {roman}")


if __name__ == '__main__':
    main()
