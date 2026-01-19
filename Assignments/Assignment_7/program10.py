################################################################################
#   Name :          DivCountEvenisible (lambda)
#   Description :   used to count even numbers from the list
#   Input :         List
#   Ouput :         NA
#   Author :        Shubham Kiran Pawar
#   Date :          19/01/2026
################################################################################

CountEven = lambda A : (A % 2 == 0)

def main():
    
    Data = [1,2,3,4,5,6,7,8]
    Result = len(list(filter(CountEven,Data)))
    print(Result)

if __name__ == "__main__":
    main()

########################################################################
# Test Cases :
#
#   Input : 1,2,3,4,5,6,7,8  Output: 4
#   
# 
#######################################################################