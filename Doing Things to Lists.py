ten_things = "Apples Oranges Crows Telephone Light Sugar"
import os
os.system("cls")
print("Wait there's not 10 things in that list, let's fix that.")

print(ten_things.split(' '))

stuff = ten_things.split(' ')
print(stuff)

more_stuff = ["Day" , "Night" , "Song" , "Frisbee" , "Corn" , "Banana" , "Girl" , "Boy"]

while len(stuff) != 10 :
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print("Therr's %d items now." %len(stuff))
    
print("There we go: " , stuff)
print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(" ".join(stuff))
print("#".join(stuff[0:2]))
    