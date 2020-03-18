path = input("Please enter file path: ")
file = open(path, "r+")
string = input("Enter string to paste into file: ")
place = int(input("Enter line number in file to place string: "))
lines_before = open(path, "r+").readlines()[:place]
lines_after = open(path, "r+").readlines()[place-1:]
new_file = "".join(lines_before) + string + "".join(lines_after)
file.write(new_file)