filename = "Exercise20.txt"
from os.path import exists

def print_all(file):
    print(file.read())

def rewind(file):
    file.seek(0)
    
def print_a_line(line_count , file):
    print(line_count , file.readline())

current_file = open(filename)

if exists(filename):
    print("Open file successfully !")
else:
    print("Error file")
    exit(1)

print("Now Let's rewind, kind of like tape.")

rewind(current_file)

print("Let's print three line:")

current_line = 1
print_a_line(current_line , current_file)

current_line += 1
print_a_line(current_line , current_file)

current_line += 1
print_a_line(current_line , current_file)

current_file.close()


