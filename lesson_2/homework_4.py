def main():
    # Get information
    year = int(input("Enter year: "))

    # Calculate century
    century = (year-1) // 100 + 1

    # display result
    print(f"\n{year} year is {century} century")


if __name__ == "__main__":
    main()
