# Procedural

def CheckEven(No):
    if(No % 2 == 0):
        print("It is even number")
    else:
        print("it is odd number")

def main():
    Value = 0

    print("Enter The number : ")
    Value = int (input())
    
    CheckEven(Value)

if(__name__ == "__main__"):
    main()