import os
import sys

def main():

    FileName = input("Enter The File Name : ")

    Data = input("Enter The String : ")

    fobj = open(FileName,"r")

    Buffer = fobj.read()
    Count = Buffer.count(Data)

    print("Frequency is : ",Count)
    
    fobj.close()    

if __name__ == "__main__":
    main()