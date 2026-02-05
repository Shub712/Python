import os

def main():
    FileName = input("Enter the name of file : ")

    if(os.path.exists(FileName)):
        fobj = open(FileName,"r")

        print(fobj.name)    # Demo.txt
        print(fobj.mode)    # r
        print(fobj.closed)  # False

        fobj.close()        # True
        print(fobj.closed)
        
    else:
        print("there is no such file")

if __name__ == "__main__":  
    main()