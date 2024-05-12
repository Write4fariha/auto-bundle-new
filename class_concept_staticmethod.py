# Learning class static concept

class calc:

    def __init__(self,y,z):
            self.y=y
            self.z=z
            print("I am in init function")
            print("value of Y in init fucntion",y)
    
#defining arg local to add class function
 
    def add(self,a,b):
            print("I am in Add Function")
            print("Value of A in add function",a)
            print("value of B in add function",b)
            print(a+b)
    
    def mul(self):
        print("I am in MUL Function")
        print("Value of Y in mul function",self.y)

def main():
      
      obj1=calc(100,50)
      obj1.add(20,30)
      obj1.mul()

if__name__="__main__"
main()