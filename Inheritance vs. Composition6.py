#Multiple Inheritance
import os
os.system("cls")

class Vietnam (object) :
    #constructer
    def __init__ (self , name) :
        self.name1 = name
    
    #display
    def Display (self) :
        print("Name in Vietnam: %s" %self.name1)
        
class America (object) :
    #constructer
    def __init__ (self , name) :
        self.name2 =  name
    
    #display
    def Display (self) :
        print("Name in America: %s" %self.name2)
        
class Person (Vietnam , America) :
    #Constructer
    def __init__ (self , name_1 , name_2) :
        
        Vietnam.__init__(self , name_1)
        
        America.__init__(self , name_2)
        
    #Display
    def Display (self) :
        
        Vietnam.Display(self)
        
        America.Display(self)
        
        
person = Person('HieuPham', 'Hieu')
person.Display()