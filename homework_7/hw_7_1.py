import string
import secrets


def char_set():
    """
    This function used to select password charset
    :return: string charset, str
    """
    print("\nSelect one of these characters sets for your password:\n")
    print("1 - lowercase letters")
    print("2 - lowercase and uppercase letters")
    print("3 - lowercase letters and digits")
    print("4 - lowercase and uppercase letters and digits")
    while True:
        try:
            charset = input("\nEnter number of your choice or press Enter to exit: ")
            if charset == "1":
                return string.ascii_lowercase
            elif charset == "2":
                return string.ascii_letters
            elif charset == "3":
                return string.ascii_lowercase + string.digits
            elif charset == "4":
                return string.ascii_letters + string.digits
            elif charset == "":
                decision = confirm("Do you want to exit? ")
                if decision == True:
                    print("\nHave a nice day!\n")
                    exit()
            else:
                raise ValueError
        except ValueError:
            print("\a\n\x1b[1;31mWrong choice!\x1b[0;37m")


def pass_gen(size, charset):
    """
    This function generates new password using Secrets module
    :param size: password size
    :param charset: password charset, i.e. string.ascii_letters or string.ascii_lowercase + string.digits
    :return: password, str
    """
    password = ''.join(secrets.choice(charset) for i in range(size))
    return password


def pass_size():
    """
    Function for setting password size
    :return: number of characters for the new password, int
    """
    while True:
        try:
            size = input("Enter password length, minimum 4, or press Enter to exit: ")
            if size == "":
                decision = confirm("Do you want to exit? ")
                if decision == True:
                    print("\nHave a nice day!\n")
                    exit()
                else:
                    continue
            else:
                size = int(size)
            if size < 4:
                raise ValueError
            else:
                return size
        except ValueError:
            print("\a\n\x1b[1;31mEntered value is incorrect!\x1b[0;37m\n")


def confirm(prompt):
    """
    Function for universal Yes/No prompts
    :param prompt: Prompt text
    :return: Y is True, N is False
    """
    while True:
        try:
            yes_no = input(f"{prompt}(Y/N): ").lower()
            if yes_no == "n":
                return False
            elif yes_no == "y":
                return True
            else:
                raise ValueError
        except ValueError:
            print("\a\n\x1b[1;31mWrong answer!\x1b[0;37m\n")


def main():
    size = pass_size()
    charset = char_set()
    pw = pass_gen(size, charset)
    while True:
        print(f"\nYour new password is \x1b[1;33m{pw}\x1b[0;37m\n")
        decision = confirm("Do you want to generate one more password? ")
        if decision == True:
            decision = confirm("Do you want to change password size? ")
            if decision == True:
                size = pass_size()
            decision = confirm("Do you want to select different charset? ")
            if decision == True:
                charset = char_set()
        else:
            break
        pw = pass_gen(size, charset)

    print("\nHave a nice day!\n")


if __name__ == '__main__':
    main()
