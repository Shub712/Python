####################################################
#   Function Name : Factorial
#   Description :   Used to find the factorial
#   Input :         Int
#   Output :        int
#   Author :        Shubham Kiran Pawar
#   Date :          25/01/2026
####################################################

def Factorial(No):
    fact = 1
    for i in range(1,No+1):
        fact = fact * i

    return fact
def main():
    print(Factorial(5))

if __name__ == "__main__":
    main()