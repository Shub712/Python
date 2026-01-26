###########################################################
#
#   Function Name : SumX
#   Description :   Used to return sum of elements of list
#   Input :         (int)List
#   Ouput :         Integer
#   Author :        Shubham Kiran Pawar   
#   Date :          26/01.2026
#
###########################################################

def SumX(Value):
    total = 0

    for i in range(len(Value)):
        total =  total + Value[i]

    return total

def main():
    Data = list()
    Size = 0

    print("Enter The Number of elements : ")
    Size = int(input())

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Ret = SumX(Data)

    print("Addition is : ", Ret)

if __name__ == "__main__":
    main()

#########################################################
#   Test Cases :
#   
#   Input : (10,20,30)      Output :    Addition is : 60
#
#
#########################################################
