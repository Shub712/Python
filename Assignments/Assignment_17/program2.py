####################################################
#   Function Name : Display
#   Description :   Used to print pattern
#   Input :         Int
#   Output :        NA
#   Author :        Shubham Kiran Pawar
#   Date :          25/01/2026
####################################################

def Display(Row):

    for i in range(1,Row+1):

        for i in range(1,Row+1):

            print("* ",end="")

        print()


def main():
    Display(5)

if __name__ == "__main__":
    main()

################################################
#
#   Test Cases : 
#   
#   Input : 5  Output : * * * * * 
#                       * * * * * 
#                       * * * * * 
#                       * * * * * 
#                       * * * * * 
#
#
#
################################################
