####################################################
#   Function Name : Display
#   Description :   Used to display the pattern
#   Input :         Int
#   Output :        NA
#   Author :        Shubham Kiran Pawar
#   Date :          25/01/2026
####################################################

def Display(Row):

    for i in range(1,Row+1):

        for i in range(1,Row+1):

            print( i,end=" ")
            
        print()


def main():
    Display(5)

if __name__ == "__main__":
    main()

################################################
#
#   Test Cases : 
#                   1 2 3 4 5 
#                   1 2 3 4 5 
#                   1 2 3 4 5 
#                   1 2 3 4 5 
#                   1 2 3 4 5  
#
################################################