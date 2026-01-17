############################################
#
#   Name of Function :  Divisible()
#   Description :       It is used to check whether number is 
#                       is divisible by 3 and 5
#   Input :             Integer
#   Ouput :             Integer
#   Author:             Shubham Kiran Pawar
#   Date :              17/01/2026
#
############################################

def Divisible(No1):
    if((No1 % 3)==0 and (No1 % 5)==0):
        print("It is divisible by 3 and 5")
    else:
        print("It is NOT divisible by 3 and 5")
        
def main():
    Divisible(17)

if __name__ == "__main__":
    main()

#################################################
##
##  Test Cases  :
##
##  Input : 15       Output :    "It is divisible by 3 and 5"
##  Input : 17       Output :    "It is NOT divisible by 3 and 5"
##
##
#################################################
