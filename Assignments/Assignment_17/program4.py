####################################################
#   Function Name : SumFactors
#   Description :   Used to find the sum of factors
#   Input :         Int
#   Output :        int
#   Author :        Shubham Kiran Pawar
#   Date :          25/01/2026
####################################################

def SumFactors(No):
    Add = 0
    for i in range(1,No+1 // 2):
        if(No % i == 0):
            Add = Add + i

    return Add

def main():
    print(SumFactors(12))

if __name__ == "__main__":
    main()