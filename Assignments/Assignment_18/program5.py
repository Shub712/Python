###########################################################
#
#   Function Name : ListPrime
#   Description :   Used to return addition of prime numbers
#   Input :         (int)List
#   Ouput :         Integer
#   Author :        Shubham Kiran Pawar   
#   Date :          26/01.2026
#
###########################################################
from MarvellousNum import CheckPrime

def ListPrime(Data):
    Sum = 0
       
    for i in Data:
        if CheckPrime(i):
            Sum = Sum + i
            
    return Sum

def main():
    Data = []
    Size = 0

    print("Enter The Number of elements : ")
    Size = int(input())

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Ret = ListPrime(Data)

    print("Addition of prime numbers is : ", Ret)

if __name__ == "__main__":
    main()

#########################################################
#   Test Cases :
#   
#   Input : (3,5,9)     Output : Addition of prime numbers is : 8
#
#
#########################################################
