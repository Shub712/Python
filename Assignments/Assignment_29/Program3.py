import os
import sys

def main():

    if(len (sys.argv )!= 2):
        print("Please Give Valid Command")

    else:
        fobj = open(sys.argv[1],"r")
        Buffer = fobj.read()

        fobj1 = open("Hello.txt","w")

        fobj1.write(Buffer)

if __name__ == "__main__":
    main()