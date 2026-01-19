##########################################################################
#   Name :          Odd (lambda)
#   Description :   used to give Odd number of given list
#   Input :         List
#   Ouput :         List
#   Author :        Shubham Kiran Pawar
#   Date :          19/01/2026
#########################################################################

Odd = lambda Data : (Data % 2 != 0)

def main():
    
    Data = [1,2,3,4,5,6,7,8]
    Result = list (filter(Odd,Data))
    print(Result)

if __name__ == "__main__":
    main()


########################################################################
# Test Cases :
#
#   Input :  [1,2,3,4,5,6,7,8] Output: [1, 3, 5, 7]
#   
# 
#######################################################################