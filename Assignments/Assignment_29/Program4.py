import os
import sys
import hashlib

def CheckSum():
    pass

def main():

    if(len (sys.argv )!= 3):
        print("Please Give Valid Command")

    else:
        fobj = open(sys.argv[1],"r")
        Buffer1 = fobj.read()

        fobj1 = open(sys.argv[2],"r")
        Buffer2 =fobj1.read()

    if(Buffer1 == Buffer2):
        print("Success")
    else:
        print("Failure")

if __name__ == "__main__":
    main()