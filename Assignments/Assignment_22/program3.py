class Arithematic:

    def __init__(self):
        self.Value1 = 0 
        self.Value2 = 0

    def Accept(self,A,B):
        self.Value1 = A
        self.Value2 = B 

    def Addition(self):
        return self.Value1 + self.Value2
    
    def Substraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        if self.Value1 == 0 or self.Value2 == 0 :
            print("Cannot perform addition of 0")
            return
        return self.Value1 // self.Value2

def main():
    obj1 = Arithematic()

    obj1.Accept(15,4)
    print(obj1.Addition())
    print(obj1.Substraction())
    print(obj1.Multiplication())
    print(obj1.Division())

if __name__ == "__main__":
    main()