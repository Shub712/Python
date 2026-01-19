##########################################################################
#   Name :          Even (lambda)
#   Description :   used to check whether number is even or not
#   Input :         Integer
#   Ouput :         NA
#   Author :        Shubham Kiran Pawar
#   Date :          19/01/2026
#########################################################################

Even = lambda No1 : (No1 % 2 == 0)

def main():

    Value1 = 15

    Ret = Even(Value1)

    if(Ret == True):
        print("Number is even")

    else:
        print("Number is Not even")

if __name__ == "__main__":
    main()

####################################################
# Test Cases :
#
#   Input : 10  Output :  Number is Even
#   Input : 17  Output :  Number is not even
# 
####################################################