##############################################################################
#
#   Name of Function :  CheckPerfect()
#   Description :       It is used to check whether number is perfect or not
#   Input :             integer
#   Ouput :             Integer
#   Author:             Shubham Kiran Pawar
#   Date :              17/01/2026
#
#############################################################################

def CheckPerfect(No):

    if(No <= 0):
        return False
    
    Sum = 0
    for i in range(1,No//2+1):
        if(No % i == 0):
            Sum = Sum + i

    if(Sum == No):
       return True
    else:
       return False
    
def main():

    Value1 = 0 
    print("Enter The number : ")
    Value1 = int (input())

    Ret = CheckPerfect(Value1)
    if(Ret == True):
       print("It is perfect number")
    else:
       print("It is not a perfect number")

if __name__ == "__main__":
    main()

############################################################################
##
##  Test Cases  :
##
##  Input : 6       Output : it is a perfect number
##  Input : 5       Output : it is not a perfect number 
##
###########################################################################