##########################################################################
#   Name :          Add (lambda)
#   Description :   used to give addition of 2 numbers
#   Input :         Integer
#   Ouput :         Integer
#   Author :        Shubham Kiran Pawar
#   Date :          19/01/2026
#########################################################################

Add = lambda No1,No2 : No1+No2

def main():

    Value1 = 13
    Value2 = 16

    Ret = Add(Value1,Value2)

    print("Addition is : ", Ret)

if __name__ == "__main__":
    main()

####################################################
# Test Cases :
#
#   Input : 10,11  Output :  Addition is 21
#   Input : 17,17  Output :  Addition is 34
# 
####################################################