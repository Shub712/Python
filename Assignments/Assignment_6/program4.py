##########################################################################
#   Name :          Min (lambda)
#   Description :   used to return Minimum of a number 2 numbers
#   Input :         Integer
#   Ouput :         Integer
#   Author :        Shubham Kiran Pawar
#   Date :          19/01/2026
#########################################################################

Min = lambda No1,No2 : No1 < No2

def main():

    Value1 = 18
    Value2 = 15

    Ret = Min(Value1,Value2)

    if(Ret == True):
        print(Value1)

    else:
        print(Value2)

if __name__ == "__main__":
    main()

####################################################
# Test Cases :
#
#   Input : 5 ,10  Output :  5
#   Input : 10,17  Output :  10
# 
####################################################