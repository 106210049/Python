#Using super() function with __init__() in inheritance
import os
os.system("cls")

#Create Person which is a inherichy class
class Person (object) :
    #Constructer
    def __init__ (self , name) :
        self.name = name
    
    #Display function
    def Display(self) :
        print("Full name: %s" %self.name)

#create Student which is a class inheri from Person class
class Student (Person) :
    #Constructer
    def __init__(self , name , score) :
        super(Student , self).__init__(name)
        self.score = score
    
    #Display function
    def Display(self) :
        super(Student , self).Display()
        print("Hight score: %d" %self.score)
        
#Main function

student = Student("Pham Doan Minh Hieu" , 10)    
student.Display()
