################################################################################
#   Name :          Divisible (lambda)
#   Description :   used to give return numbers which divisible ny 3 and 5
#   Input :         List
#   Ouput :         List
#   Author :        Shubham Kiran Pawar
#   Date :          19/01/2026
################################################################################

Divisible = lambda A: (A % 3 == 0) and (A % 5 == 0)

def main():
    
    Data = [3,15,9,20]
    Result = list (filter(Divisible,Data))
    print(Result)

if __name__ == "__main__":
    main()

########################################################################
# Test Cases :
#
#   Input :  3,15,9,20   Output:  15
#   
# 
#######################################################################