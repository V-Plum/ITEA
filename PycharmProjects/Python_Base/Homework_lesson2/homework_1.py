def main():
    # Show task
    task = "3x^2 + 12x + 10 = 0"
    print(f"Let's take this quadratic equation as an example: {task} \n")

    # Find and show discriminant
    d = 12 ** 2 - 4 * 3 * 10
    print(f"Discriminant = {d} \n")

    # Discriminant is > 0, so there are two results
    x1 = ((0-12) + d ** 0.5) / (2 * 3)
    x2 = ((0-12) - d ** 0.5) / (2 * 3)
    print(f"x1 = {x1}")
    print(f"x2 = {x2}\n")

    # second part is to solve any quadratic equation
    print("And now let's resolve any quadratic equation. Please, enter variables for this template:\nax^2 + bx + c = 0")

    # Input and checking if a not equal to 0
    a = int(input("Enter a: "))
    while a == 0:
        print("Sorry, a cannot be equal to 0.")
        a = int(input("Enter a again: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))

    # Find and show discriminant
    d = b ** 2 - 4 * a * c
    print(f"\nDiscriminant = {d}\n")

    # If discriminant > 0 then we will have X1 and X2
    if d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")

    # If discriminant = 0 then we will have one X
    elif d == 0:
        x = -(b / (2 * a))
        print(f"x = {x}")

    # If discriminant < 0 then there are no possible results
    elif d < 0:
        print("Discriminant is negative, so X cannot be found")


if __name__ == "__main__":
    main()
