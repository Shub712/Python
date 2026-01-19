##########################################################################
#   Name :          Max (lambda)
#   Description :   used to give Maximum of 2 numbers
#   Input :         Integer
#   Ouput :         Integer
#   Author :        Shubham Kiran Pawar
#   Date :          19/01/2026
#########################################################################

Max = lambda No1,No2,No3 : max(No1,No2,No3)

def main():

    Value1 = 17
    Value2 = 20
    Value3 = 18

    Ret = Max(Value1,Value2,Value3)
    print("Maximum number is : ", Ret)

if __name__ == "__main__":
    main()

####################################################
# Test Cases :
#
#   Input : 13,16,15  Output :  16
#   Input : 17,17,89  Output :  89
# 
####################################################