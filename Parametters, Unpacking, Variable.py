from sys import argv
argv = ["How old are you?. ","How tall are you?. ","how much do you weight?. "]
str1 , str2 , str3 = argv
age = input(str1)
height = input(str2)
weight = input(str3)
print("I'm %s old, %s tall and %s heavy." % (age , height , weight))