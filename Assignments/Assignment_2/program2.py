##############################################################################
#
#   Name of Function :  Sum()
#   Description :       It is used to print summation of the natural number
#   Input :             Integer
#   Ouput :             Integer
#   Author:             Shubham Kiran Pawar
#   Date :              17/01/2026
#
#############################################################################

def Sum(No1):
    Sum = 0
    for i in range(1,No1+1):
        Sum = Sum + i

    print(Sum)    

def main():
    Sum(5)

if __name__ == "__main__":
    main()

############################################################################
##
##  Test Cases  :
##
##  Input : 5       Output :  15 
##  
##
###########################################################################
