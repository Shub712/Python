##############################################################################
#
#   Name of Function :  Sum()
#   Description :       It is used to print Odd numbers
#   Input :             Integer
#   Ouput :             Integer
#   Author:             Shubham Kiran Pawar
#   Date :              17/01/2026
#
#############################################################################

def Odd(No1):
    for i in range(1,No1+1):
        if(i % 2 != 0):
            print(i, end = ' ')    
    print()
def main():
    Odd(10)

if __name__ == "__main__":
    main()

############################################################################
##
##  Test Cases  :
##
##  Input : 10      Output :  1 3 5 7 9 
##  
##
###########################################################################
