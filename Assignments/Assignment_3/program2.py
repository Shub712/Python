##############################################################################
#
#   Name of Function :  Digits()
#   Description :       It is used to give count of a number
#   Input :             Integer
#   Ouput :             Integer
#   Author:             Shubham Kiran Pawar
#   Date :              17/01/2026
#
#############################################################################

def Digits(No1):

    if(No1 < 0):
        return 1    
    
    Count = 0

    while(No1 != 0):

        Count = Count + 1
        No1 = No1 // 10

    return Count

def main():
    Value = 0
    Value = Digits(1245)
    print("The Count is : ", Value)

if __name__ == "__main__":
    main()

############################################################################
##
##  Test Cases  :
##
##  Input : 103      Output :   The count is 3
##  Input : 11      output  :   The count is 2
##
###########################################################################
