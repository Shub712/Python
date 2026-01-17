##############################################################################
#
#   Name of Function :  Area()
#   Description :       It is used to calculate area of arectangle
#   Input :             integer
#   Ouput :             Integer
#   Author:             Shubham Kiran Pawar
#   Date :              17/01/2026
#
#############################################################################

def Area(No1,No2):

    Area = No1 * No2
    return Area

def main():

    Value1 = 0 
    Value2 = 0
    Ret = 0
    print("Enter The length : ")
    Value1 = int (input())

    print("Enter The Wifth : ")
    Value2 = int (input())

    Ret = Area(Value1, Value2)
    print("The area of a rectangle is : ", Ret)

if __name__ == "__main__":
    main()

############################################################################
##
##  Test Cases  :
##
##  Input : 12,13          Output : The area of a rectangle is 156 
##
###########################################################################