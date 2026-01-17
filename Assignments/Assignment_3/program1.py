##############################################################################
#
#   Name of Function :  Prime()
#   Description :       It is used to check whether number is prime number or not
#   Input :             Integer
#   Ouput :             Integer
#   Author:             Shubham Kiran Pawar
#   Date :              17/01/2026
#
#############################################################################

def Prime(No1):
    bValue  = False
    if(No1 % 2 == 0):
        return bValue

    bValue = True
    return bValue

def main():
    bRet = False

    bRet = Prime(12)

    if(bRet == True):
        print("it is a prime number")
    else:
        print("It is not a prime number")

if __name__ == "__main__":
    main()

############################################################################
##
##  Test Cases  :
##
##  Input : 10      Output :    It is not a prime number
##  Input : 11      output  :   It is prime number
##
###########################################################################
