##########################################################################
#   Name :          Square (lambda)
#   Description :   used to give square of given list
#   Input :         List
#   Ouput :         List
#   Author :        Shubham Kiran Pawar
#   Date :          19/01/2026
#########################################################################
Square = lambda Data : Data ** 3

def main():

    Data = [2,4,5,6,7]
    Ret = list (map(Square,Data))
    print(Ret)

if __name__ == "__main__":
    main()


####################################################
# Test Cases :
#
#   Input : 2,4,5,6,7  Output : [8, 64, 125, 216, 343]
#   
# 
####################################################