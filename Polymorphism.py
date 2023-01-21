class Rabbit (object) :
    
    def age (self) :
        print("The function has determines the age of Rabbit.")
     
    def color (self) :
        print("The function has determines the color of Rabbit.")
        
class Horse (object) :
    
    def age (self) :
        print("The function has determines the age of Horse.")
    
    def color (self) :
        print("The function has determines the color of Horse")
        
obj1 = Rabbit()
obj2 = Horse()

for type in (obj1 , obj2) :
    type.age()
    type.color()
