with open("tasks.txt", "a") as f:
    f.write("I might read a book later today.\n")
    f.write("I hope tomorrow will be even better.\n")

with open("tasks.txt", "r") as f:
    print("Content after appending:")
    print(f.read())