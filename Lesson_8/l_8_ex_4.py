import re


def find_iterations(string, pattern):
    count = re.subn(pattern, '', string)[1]
    return count


string = input("Enter string: ")
pattern = input("Enter text to find: ")
print(find_iterations(string, pattern))