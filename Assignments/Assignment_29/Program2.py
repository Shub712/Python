import os

def main():
    try:
        FileName = input("Enter The File Name : ")

        fobj = open("Demo.txt","r")

        if(os.path.exists(FileName)):
            print("The File is exists in the current directory")
        else:
            print("The File Doesnt exist in the current directory")
        
        Buffer = fobj.read()

        print("Data is : ",Buffer)

    except FileNotFoundError:
        print("There is no sus=ch file")


if __name__ == "__main__":
    main()