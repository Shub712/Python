##############################################################################
#
#   Name of Function :  Table()
#   Description :       It is used to print the table of a number
#   Input :             Integer
#   Ouput :             Integer
#   Author:             Shubham Kiran Pawar
#   Date :              17/01/2026
#
#############################################################################

def Table(No1):
    
    for i in range(1,11):
        print(No1 * i)
        
def main():
    Table(17)

if __name__ == "__main__":
    main()

############################################################################
##
##  Test Cases  :
##
##  Input : 17       Output :   17
##                              34
##                              51
##                              68
##                              85
##                              102
##                              119
##                              136
##                              153
##                              170
##  
##
###########################################################################
