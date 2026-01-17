##############################################################################
#
#   Name of Function :  Factor()
#   Description :       It is used to display the factor of a number
#   Input :             integer
#   Ouput :             Nothing
#   Author:             Shubham Kiran Pawar
#   Date :              17/01/2026
#
#############################################################################

def Factor(No1):
    
    for i in range(1,No1+1):
        if(No1 % i == 0):
            print(i, end = " ")
    print()

def main():

   Factor(12)

if __name__ == "__main__":
    main()

############################################################################
##
##  Test Cases  :
##
##  Input : 12          Output :   1 2 3 4 6 12 
##
###########################################################################