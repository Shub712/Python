import os

def main():
    
    FileName = input("Enter The File Name :")

    if(os.path.exists(FileName)):
        print("The File is exists in the current directory")
    else:
        print("The File Doesnt exist in the current directory")

if __name__ == "__main__":
    main()