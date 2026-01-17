##############################################################################
#
#   Name of Function :  Summation()
#   Description :       It is used to give Sum of a numbers
#   Input :             Integer
#   Ouput :             Integer
#   Author:             Shubham Kiran Pawar
#   Date :              17/01/2026
#
#############################################################################

def Summation(No1):

    if(No1 < 0):
        return 1    
    
    Sum = 0
    Digit = 0

    while(No1 != 0):

        Digit = No1 % 10
        Sum = Sum + Digit
        No1 = No1 // 10

    return Sum

def main():
    Value = 0
    Value = Summation(655)
    print("The Sum is : ", Value)

if __name__ == "__main__":
    main()

############################################################################
##
##  Test Cases  :
##
##  Input : 103      Output :    The sum is 4
##  Input : 115      output  :   The Sum is 7
##
###########################################################################
