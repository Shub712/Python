class Numbers:

    def __init__(self,A):
        self.Value = A 

    def CheckPrime(self):

        if(self.Value < 2):
            return False

        for i in range(2,int(self.Value  / 2 )+1):
            if(self.Value % i == 0):
                return False
        
        return True
        
    def ChkPerfect(self):

        Sum = 0

        for i in range(1,(self.Value//2)+1):
            if(self.Value % i == 0):
                Sum = Sum + i
        
        if(Sum == self.Value):
            return True
        
        else:
            return False
        
    def Factors(self):
        for i in range(1,self.Value+1):
            if(self.Value % i == 0):
                print(i)
    
    def SumFactors(self):
        Sum = 0

        for i in range(1,self.Value+1):
            if(self.Value % i == 0):
                Sum = Sum + i
        
        return Sum


def main():
    obj1= Numbers(6)

    print(obj1.CheckPrime())
    print(obj1.ChkPerfect())

    obj1.Factors()

    Ret = obj1.SumFactors()
    print(Ret)


if __name__ == "__main__":
    main()