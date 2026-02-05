import os

def main():
    FileName = input("Enter the name of file : ")

    if(os.path.exists(FileName)):
        os.remove(FileName)
        print("File removed successfully")
                    
    else:
        print("there is no such file")

if __name__ == "__main__":  
    main()