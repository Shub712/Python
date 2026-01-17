##############################################################################
#
#   Name of Function :  CheckVowel()
#   Description :       It is used to check whether character is vowel or not
#   Input :             Char
#   Ouput :             Nothing
#   Author:             Shubham Kiran Pawar
#   Date :              17/01/2026
#
#############################################################################

def CheckVowel(cValue):
    bFlag = False
    if(cValue == 'a' or cValue == 'e' or cValue == 'i'or cValue == 'o'or cValue == 'u'):
        bFlag = True
    else:
        bFlag = False

    return bFlag
def main():

    bRet = CheckVowel('h')
    
    if(bRet == True):
        print("It is vowel")
    else:
        print("It is not vowel")

if __name__ == "__main__":
    main()

############################################################################
##
##  Test Cases  :
##
##  Input : 'a'          Output :   it is a vowel
##  Input : 'g'          Output  :  It is not a vowel
##
###########################################################################