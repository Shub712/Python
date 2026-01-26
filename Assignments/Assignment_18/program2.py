###########################################################
#
#   Function Name : maxX
#   Description :   Used to return maximum number from list
#   Input :         (int)List
#   Ouput :         Integer
#   Author :        Shubham Kiran Pawar   
#   Date :          26/01.2026
#
###########################################################

def maxX(Value):
    Maximum = Value[0]

    for i in range(len(Value)):
        if(Value[i]>Maximum):
            Maximum = Value[i]

    return Maximum

def main():
    Data = list()
    Size = 0

    print("Enter The Number of elements : ")
    Size = int(input())

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    Ret = maxX(Data)

    print("maximum number is : ", Ret)

if __name__ == "__main__":
    main()

#########################################################
#   Test Cases :
#   
#   Input : (10,20,30)      Output :    maximum is : 30
#
#
#########################################################
