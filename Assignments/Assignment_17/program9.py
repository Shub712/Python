####################################################
#   Function Name : CountNum
#   Description :   Used to count the nubers from the digits
#   Input :         Int
#   Output :        Int
#   Author :        Shubham Kiran Pawar
#   Date :          25/01/2026
####################################################

def CountNum(No):
    Count = 0

    while(No != 0):

        No = No // 10
        Count = Count + 1

    return Count
def main():
    
   print(CountNum(24254262))

if __name__ == "__main__":
    main()

################################################
#
#   Test Cases : 
#   
#   Input : 5678        Output : 4
################################################