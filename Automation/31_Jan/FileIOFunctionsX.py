import os

def main():
    FileName = input("Enter the name of file : ")

    if(os.path.exists(FileName)):
        fobj = open(FileName,"w")

        print(fobj.readable())  # True
        print(fobj.writable())  # False
        print(fobj.seekable())  # True

    else:
        print("there is no such file")

if __name__ == "__main__":  
    main()