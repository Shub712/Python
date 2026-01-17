##############################################################################
#
#   Name of Function :  Palindrome()
#   Description :       It is used to check whether number is palindrome or not
#   Input :             Integer
#   Ouput :             Integer
#   Author:             Shubham Kiran Pawar
#   Date :              17/01/2026
#
#############################################################################

def Palindrome(No1):

    bValue = False

    if(No1 < 0):
        return 1    
    
    Original = No1
    Sum = 0

    while(No1 != 0):

        Digit = No1 % 10
        Sum = Sum * 10 + Digit
        No1 = No1 // 10

    if(Original == Sum):
        bValue = True

    else:
        bValue = False
    
    return bValue

def main():
    bRet = False
    bRet = Palindrome(121)
    
    if(bRet == True):
        print("it is palindrome number")

    else:
        print("it is not a palindrome number")

if __name__ == "__main__":
    main()

############################################################################
##
##  Test Cases  :
##
##  Input : 212      Output :    It is palindrome number
##  Input : 115       Output  :  It is not a palindrome number
##
###########################################################################
