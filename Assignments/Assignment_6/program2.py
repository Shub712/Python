####################################################
#   Name :          Cube (lambda)
#   Description :   used to return cube of a number
#   Input :         Integer
#   Ouput :         Integer
#   Author :        Shubham Kiran Pawar
#   Date :          19/01/2026
####################################################

Cube = lambda No : No ** 3

def main():

    Ret = Cube(int(input("Enter The number: ")))
    print ("The Cube is : ", Ret)

if __name__ == "__main__":
    main()

####################################################
# Test Cases :
#
#   Input : 5   Output :  125
#   Input : 10  Output :  1000
#   Input : 10  Output :  216
####################################################