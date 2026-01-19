##########################################################################
#   Name :          Product (lambda)
#   Description :   used to give Product numbers of given list
#   Input :         List
#   Ouput :         NA
#   Author :        Shubham Kiran Pawar
#   Date :          19/01/2026
#########################################################################

from functools import reduce

Product = lambda A,B : A * B 

def main():
    
    Data = [1,6,3,4]
    Result = reduce(Product,Data)
    print(Result)

if __name__ == "__main__":
    main()

########################################################################
# Test Cases :
#
#   Input :  [1,6,3,4]  Output:  72
#   
# 
#######################################################################