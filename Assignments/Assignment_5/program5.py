##############################################################################
#
#   Name of Function :  Grade()
#   Description :       It is used to display grades
#   Input :             integer
#   Ouput :             NA
#   Author:             Shubham Kiran Pawar
#   Date :              17/01/2026
#
#############################################################################

def Grade(No):

    if(No>=75):
        print("Distinction")
    elif(No>=60):
        print("First Class grade")
    elif(No>=50):
        print("Second Class grade")
    else:
        print("Fail")

def main():
    Grade(75)

if __name__ == "__main__":
    main()
    
############################################################################
##
##  Test Cases  :
##
##  Input : 75       Output : Distinction
##  Input : 48       Output : Fail 
##
###########################################################################