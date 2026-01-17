##############################################################################
#
#   Name of Function :  DecToBinary()
#   Description :       It is used to convert decimal into binary
#   Input :             integer
#   Ouput :             Integer
#   Author:             Shubham Kiran Pawar
#   Date :              17/01/2026
#
#############################################################################

def DecToBinary(No):
    Arr = []

    while(No > 0):
        bit = No % 2
        Arr.append(str(bit))
        No //=2

    Arr.reverse()
    return "".join(Arr)

def main():
    print(DecToBinary(11))

if __name__ == "__main__":
    main()
    
############################################################################
##
##  Test Cases  :
##
##  Input : 11       Output : 1011
##  Input : 12       Output : 1100 
##
###########################################################################