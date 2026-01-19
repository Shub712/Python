##########################################################################
#   Name :          Minimum (lambda)
#   Description :   used to give Minimum number of given list
#   Input :         List
#   Ouput :         NA
#   Author :        Shubham Kiran Pawar
#   Date :          19/01/2026
#########################################################################

from functools import reduce

Minimum = lambda A,B: A if(A<B) else B

def main():
    
    Data = [1,6,3,4]
    Result = reduce(Minimum,Data)
    print(Result)

if __name__ == "__main__":
    main()

########################################################################
# Test Cases :
#
#   Input :  [1,2,3,4] Output:  1
#   
# 
#######################################################################