##########################################################################
#   Name :          Divisible (lambda)
#   Description :   used to check whether number is divisible by 5 or not
#   Input :         Integer
#   Ouput :         NA
#   Author :        Shubham Kiran Pawar
#   Date :          19/01/2026
#########################################################################

Divisible = lambda No1 : (No1 % 5 == 0)

def main():

    Value1 = 13

    Ret = Divisible(Value1)

    if(Ret == True):
        print("Number is divisible by 5")

    else:
        print("Number is Not divisible by 5")

if __name__ == "__main__":
    main()

####################################################
# Test Cases :
#
#   Input : 10  Output :  Number is divisible by 5
#   Input : 17  Output :  Number is Not divisible by 5
# 
####################################################