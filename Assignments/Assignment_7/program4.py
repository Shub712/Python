##########################################################################
#   Name :          Addition (lambda)
#   Description :   used to give Addition number of given list
#   Input :         List
#   Ouput :         NA
#   Author :        Shubham Kiran Pawar
#   Date :          19/01/2026
#########################################################################

from functools import reduce

Addition = lambda A,B: A+B 

def main():
    
    Data = [1,2,3,4]
    Result = reduce(Addition,Data)
    print(Result)

if __name__ == "__main__":
    main()

########################################################################
# Test Cases :
#
#   Input :  [1,2,3,4] Output:  10
#   
# 
#######################################################################