##############################################################################
#
#   Name of Function :  Reverse()
#   Description :       It is used to reverse the digit
#   Input :             Integer
#   Ouput :             Integer
#   Author:             Shubham Kiran Pawar
#   Date :              17/01/2026
#
#############################################################################

def Reverse(No1):

    if(No1 < 0):
        return 1    
    
    Sum = 0

    while(No1 != 0):

        Digit = No1 % 10
        Sum = Sum * 10 + Digit
        No1 = No1 // 10

    return Sum

def main():
    Value = 0
    Value = Reverse(655)
    print("The Sum is : ", Value)

if __name__ == "__main__":
    main()

############################################################################
##
##  Test Cases  :
##
##  Input : 4562      Output :  2654
##  Input : 115      output  :  511
##
###########################################################################
