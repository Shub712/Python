class Demo :
    Value = 11

    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B
    
    def fun(self):
        print(self.No1)
        print(self.No2)

    def gun(self):
        print(self.No1)
        print(self.No2)


def main():

    obj1 = Demo(11,21)
    obj2 = Demo(51,101)

    obj1.fun()
    obj2.gun()
    obj1.gun()
    obj2.gun()

if __name__ == "__main__":
    main()