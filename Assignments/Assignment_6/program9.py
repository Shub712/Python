##########################################################################
#   Name :          Multiplication (lambda)
#   Description :   used to give Multiplication of 2 numbers
#   Input :         Integer
#   Ouput :         Integer
#   Author :        Shubham Kiran Pawar
#   Date :          19/01/2026
#########################################################################

Multiplication = lambda No1,No2 : No1*No2

def main():

    Value1 = 13
    Value2 = 16

    Ret = Multiplication(Value1,Value2)

    print("Multiplication is : ", Ret)

if __name__ == "__main__":
    main()

####################################################
# Test Cases :
#
#   Input : 13,16  Output :  Multiplication is 108
#   Input : 17,17  Output :  Multiplication is 289
# 
####################################################