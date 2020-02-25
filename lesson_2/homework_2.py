def main():
    # Get number
    n = int(input("Enter number: "))

    # Calculate result
    n1 = n + 1
    n2 = n - 1
    result = n1 ** 2 - n2 ** 2

    # display result
    print(f"Різниця добутків чисел n+1 та n-1 дорівнює: {result}")


if __name__ == "__main__":
    main()
