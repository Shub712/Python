##############################################################################
#
#   Name of Function :  Display()
#   Description :       It is used to Display the range
#   Input :             inteer
#   Ouput :             Integer
#   Author:             Shubham Kiran Pawar
#   Date :              17/01/2026
#
#############################################################################

def Display(No1):
    for i in range(1,No1+1):
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
##  Input : 5          Output : 1 2 3 4 5
##
###########################################################################