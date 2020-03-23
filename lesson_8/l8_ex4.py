with open("abc.txt", "r") as file:
    to_sort = file.read().split("\n")
file = open("abc.txt", "w")
add = input("Enter word: ")
to_sort.append(add)
to_sort.sort()
done = "\n".join(to_sort)
file.write(done)
file.close()
