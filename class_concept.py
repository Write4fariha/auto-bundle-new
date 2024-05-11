# Learning python class

class calc:
    
    x=50
    
    def __init__(self, y, z):
        self.y = y
        self.z = z
        print("I am in init function")
        print("Value of Y", y)

    def add(self):
        print("I am in add Function")
        print("Value of Y in add function",self.y)
        print("value of Z in add function",self.z)
        print(self.y+self.z)
    
    def mul(self):
        print("I am in MUL Function")
        print("Value of Y in mul function",self.y)
    
    def div(self):
        print("I am in DIV Function")
        print("Value of Y in div function",self.y)
    
       
def main():
    obj1 = calc(20,100)
    obj1.add()
    obj1.mul()
    obj1.div()
    print(obj1.x)

if __name__=="__main__":
    main()




