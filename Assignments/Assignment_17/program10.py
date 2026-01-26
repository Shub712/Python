####################################################
#   Function Name : SumDigit
#   Description :   Used to give summation of numbers
#   Input :         Int
#   Output :        Int
#   Author :        Shubham Kiran Pawar
#   Date :          25/01/2026
####################################################

def SumDigit(No):
    Sum = 0
    Digit = 0

    while(No != 0):
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10
    

    return Sum
def main():
    
   print(SumDigit(321))

if __name__ == "__main__":
    main()


################################################
#
#   Test Cases : 
#   
#   Input : 321        Output : 5
################################################