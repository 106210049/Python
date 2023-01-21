import os
os.system("cls")
#create a class Person
class Person (object) :
    #Contructer
    def __init__(self , name , id) :
        self.name = name
        self.id = id
    def display(self) :
        print("ID: %s, ho va ten: %s\n" %(self.id , self.name))
    def update(self , new_id , new_name) :
        self.id = new_id
        self.name = new_name

obj = Person("Pham Doan Minh Hieu" , "102210313")
obj.display()
obj.update("101111111" , "Le Huu Minh Vu")
obj.display()