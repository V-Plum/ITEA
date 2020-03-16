generated_list = []


def selector(variants, prompt, is_exit=True, own=False):
    """
    Function for selecting  answer from a list, plus optional own variant
    :param is_exit: Turns on "hei Enter to exit" option, True/False
    :param variants: list with variants, ["first", "second", ...]
    :param prompt: String with prompt or question
    :param own: is own answer possible, True/False, default is True
    :return: selected answer list index (int), selected answer (string)
    """
    for i in range(len(variants)):
        print(f"{i+1} - {variants[i]}")
    if own:
        print("0 - Own variant")
    while True:
        if is_exit:
            user_input = input(f"{prompt} or hit Enter to exit: ")
            if user_input == "":
                answer = confirm("\nAre you sure want to exit? ")
                if answer:
                    print("Exiting...")
                    exit()
                else:
                    continue
        else:
            user_input = input(f"{prompt}: ")
        try:
            user_input = int(user_input)
            if user_input > len(variants) or user_input < 0:
                raise ValueError
        except ValueError:
            print("Entered value is wrong")
            continue
        if user_input == 0 and own:
            answer = input("Enter your own variant: ")
        elif user_input == 0 and not own:
            print("Entered value is wrong")
            continue
        else:
            answer = variants[user_input-1]
        return user_input-1, answer


def int_enter(prompt, is_exit=False, allowed_min=None, allowed_max=None):
    """
    Universal function to prompt integers, optionally with min and/or max allowed values
    :param is_exit: Turns on "hei Enter to exit" option, True/False
    :param prompt: Prompt or question, string
    :param allowed_min: Min allowed number, int, default is None
    :param allowed_max: Max allowed number, int, default is None
    :return: integer, entered by user in allowed limits
    """
    if allowed_min is not None and allowed_max is not None and allowed_min > allowed_max:
        print("Min allowed value cannot be larger than Max allowed value")
        exit()
    while True:
        if is_exit:
            if allowed_min is not None and allowed_max is not None:
                entered_num = input(f"{prompt} from {allowed_min} to {allowed_max} or hit Enter to exit: ")
            elif allowed_min is not None and allowed_max is None:
                entered_num = input(f"{prompt} not less than {allowed_min} or hit Enter to exit: ")
            elif allowed_min is None and allowed_max is not None:
                entered_num = input(f"{prompt} not higher than {allowed_max} or hit Enter to exit: ")
            else:
                entered_num = input(f"{prompt} or hit Enter to exit: ")
            if entered_num == "":
                answer = confirm("\nAre you sure want to exit? ")
                if answer:
                    print("Exiting...")
                    exit()
                else:
                    continue
        else:
            if allowed_min is not None and allowed_max is not None:
                entered_num = input(f"{prompt} from {allowed_min} to {allowed_max}: ")
            elif allowed_min is not None and allowed_max is None:
                entered_num = input(f"{prompt} not less than {allowed_min}: ")
            elif allowed_min is None and allowed_max is not None:
                entered_num = input(f"{prompt} not higher than {allowed_max}: ")
            else:
                entered_num = input(f"{prompt}: ")
            if entered_num == "":
                continue
        try:
            entered_num = int(entered_num)
        except ValueError:
            print("Entered value is not a number")
            continue
        if allowed_min is not None and entered_num < allowed_min:
            print("Entered number is lower, than allowed.")
        elif allowed_max is not None and entered_num > allowed_max:
            print("Entered number is higher, than allowed.")
        else:
            return entered_num


def create_list(size=None):
    """
    Function to create lists of any size from string input
    :param size: Prompt text
    :return: list with string units
    """
    global generated_list
    if size is None:
        size = int_enter("How many items do you want to add to your list? ")
    for i in range(size):
        while True:
            value = input(f"Please enter item {i+1}: ")
            if value == "":
                answer = confirm("Is your list ready?")
                if answer:
                    return generated_list
                else:
                    continue
            generated_list.append(value)
            break
    return generated_list


def confirm(prompt):
    """
    Function for universal Yes/No prompts
    :param prompt: Prompt or question text
    :return: True for Y, False for N
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
            print("\a\nWrong answer!\n")


# example to run selector function
# a, b = selector(["First option", "Second option", "Third option"], "Select your option")
# print(a, b)

# example to run int_enter function
# num = int_enter("Please enter number")
# print(num)

# example to run create_list function
# a = create_list()
# print(a)
