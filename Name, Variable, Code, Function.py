def print_two (*list):
    var1 , var2 = list
    print("var1 = %s , var2 = %s"  %(var1 , var2))

def print_two_again (list1 , list2):
    var1 = list1
    var2 = list2
    print("var1 = %s , var2 = %s"  %(var1 , var2))
    
def print_one (list1):
    var1 = list1
    print("var1 = %s"  %var1)
    
def print_none ():
    print("I got noting.")
    
print_two("Zed" , "Shaw")
print_two_again("Zed" , "Shaw")
print_one("First!")
print_none()

    