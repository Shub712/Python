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

def Frequency(Value,A):
    count = 0

    for i in range(len(Value)):
        if(Value[i] == A):
            count = count + 1

    return count

def main():
    Data = list()
    Size = 0

    print("Enter The Number of elements : ")
    Size = int(input())

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    No = int(input("Enter The Number : "))
    Ret = Frequency(Data,No)

    print("frequency is : ", Ret)

if __name__ == "__main__":
    main()

#########################################################
#   Test Cases :
#   
#   Input : (10,20,30,10),10      Output :   frequency is 2
#
#
#########################################################
