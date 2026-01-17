# Procedural

def CheckEven(No):
    if(No % 2 == 0):
        return True
    else:
        return False

def main():
    Value = 0
    Ret = False

    print("Enter The number : ")
    Value = int (input())
    
    Ret = CheckEven(Value)

    if(Ret == True):
        print("it is even number")
    else:
        print("it is odd number") 

if(__name__ == "__main__"):
    main()