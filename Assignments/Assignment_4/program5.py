##############################################################################
#
#   Name of Function :  Display()
#   Description :       It is used to Display the range in reverse order
#   Input :             integerr
#   Ouput :             Integer
#   Author:             Shubham Kiran Pawar
#   Date :              17/01/2026
#
#############################################################################

def Display(No1):
    for i in range(-No1,0):
        print(i,end = " ")
    print()

def main():

   Display(5)

if __name__ == "__main__":
    main()

############################################################################
##
##  Test Cases  :
##
##  Input : 5          Output : -5 -4 -3 -2 -1 
##
###########################################################################