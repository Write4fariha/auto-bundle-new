# Learning class static concept

class calc:

    def __init__(self,y,z):
            self.y=y
            self.z=z
            print("I am in init function")
            print("value of Y in init fucntion",y)
    
    def add(self):
            print("I am in Add Function")
            print("Value of Y in add function",self.y)
            print("value of Z in add function",self.z)
            print(self.y+self.z)
    
    def mul(self):
        print("I am in MUL Function")
        print("Value of Y in mul function",self.y)

def main():
      
      obj1=calc(100,50)
      obj1.add()
      obj1.mul()

if__name__="__main__"
main()