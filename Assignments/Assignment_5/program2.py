##############################################################################
#
#   Name of Function :  Area()
#   Description :       It is used to calculate area of circle
#   Input :             integer
#   Ouput :             Integer
#   Author:             Shubham Kiran Pawar
#   Date :              17/01/2026
#
#############################################################################

def Area(Radius):

    PI = 3.14
    Area = PI * Radius * Radius
    return Area

def main():

    Value1 = 0 
    Value2 = 0
    Ret = 0
    print("Enter The length : ")
    Value1 = int (input())


    Ret = Area(Value1)
    print("The area of a circle is : ", Ret)

if __name__ == "__main__":
    main()

############################################################################
##
##  Test Cases  :
##
##  Input : 5       Output : The area of a Circle is 78.5 
##
###########################################################################