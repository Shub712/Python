##########################################################################
#   Name :          Odd (lambda)
#   Description :   used to check whether number is Odd or not
#   Input :         Integer
#   Ouput :         NA
#   Author :        Shubham Kiran Pawar
#   Date :          19/01/2026
#########################################################################

Odd = lambda No1 : (No1 % 2 != 0)

def main():

    Value1 = 15

    Ret = Odd(Value1)

    if(Ret == True):
        print("Number is Odd")

    else:
        print("Number is Not Odd")

if __name__ == "__main__":
    main()

####################################################
# Test Cases :
#
#   Input : 10  Output :  Number is Not odd
#   Input : 17  Output :  Number is Odd
# 
####################################################