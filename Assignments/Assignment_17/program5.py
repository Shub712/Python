####################################################
#   Function Name : ChkPrime
#   Description :   Used to find the prime number
#   Input :         Int
#   Output :        int
#   Author :        Shubham Kiran Pawar
#   Date :          25/01/2026
####################################################

def ChkPrime(No):

    for i in range(2,No):
        if(No % i == 0):
            return False

    return True
def main():
    Ret = (ChkPrime(5))

    if (Ret == True):
         print("it is a prime number")

    else:
        print("It is not a prime number")

if __name__ == "__main__":
    main()