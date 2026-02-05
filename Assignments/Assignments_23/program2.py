class BankAccount:
    ROI = 10.5

    def __init__(self,A,B):
        self.Name = A 
        self.Amount = B

    def Display(self):
        print("Account Holders Name : ",self.Name)
        print("Current Balance is : ",self.Amount)

    def Deposit(self,A):
        self.Amount = self.Amount + A
    
    def Withdraw(self,B):
        if(B>self.Amount):
            print("Cannot withdraw" ,B,"Because of Insuffiecient Funds")
            return
        self.Amount = self.Amount - B

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest


def main():
    obj1 = BankAccount("Shubham Pawar",34000)
    obj1.Display()

    obj1.Deposit(12000)
    obj1.Display()

    obj1.Withdraw(3000)
    obj1.Display()

    print(obj1.CalculateInterest())

    obj1.Withdraw(45000)
    obj1.Display()


if __name__ == "__main__":
    main()