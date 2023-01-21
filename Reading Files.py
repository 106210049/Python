from sys import argv
argv = "Reading_Files.txt"
file_name = argv
txt = open(file_name)
print("Here's your file %r: " %file_name)
print(txt.read())
print("Type a filename again: ")
file_again = input(">")
txt_again = open(file_again)
print(txt_again.read())
