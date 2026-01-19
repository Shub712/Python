################################################################################
#   Name :          Length (lambda)
#   Description :   used to give return string which characters are less than 5
#   Input :         List
#   Ouput :         List
#   Author :        Shubham Kiran Pawar
#   Date :          19/01/2026
################################################################################

Length = lambda A: (len(A) < 5 )

def main():
    
    Data = ["hello", "Demo", "hi","Shubham"]
    Result = list (filter(Length,Data))
    print(Result)

if __name__ == "__main__":
    main()

########################################################################
# Test Cases :
#
#   Input :  ["hello", "Demo", "hi","Shubham"]   Output:  Demo, hi
#   
# 
#######################################################################