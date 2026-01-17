##############################################################################
#
#   Name of Function :  Sum()
#   Description :       It is used to print factorial of number
#   Input :             Integer
#   Ouput :             Integer
#   Author:             Shubham Kiran Pawar
#   Date :              17/01/2026
#
#############################################################################

def Fact(No1):
    Sum = No1
    for i in range(1,No1):
        Sum = Sum * i

    print(Sum)    

def main():
    Fact(5)

if __name__ == "__main__":
    main()

############################################################################
##
##  Test Cases  :
##
##  Input : 5       Output :  120 
##  
##
###########################################################################
