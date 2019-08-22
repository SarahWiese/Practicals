# 1
input_file = open("name.txt", "w")
name = input("What is your name: ")
print(name, file=input_file)
input_file.close()

# 2
input_file = open("name.txt", "a")
input_file.read()
print("Your name is {}".format(name), file=input_file)
input_file.close()

# 3
in_file = open("numbers.txt", "r")
in_file.readlines()
