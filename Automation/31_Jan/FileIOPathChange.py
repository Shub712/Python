import os

def main():
    FileName = input("Enter the name of file : ")

    if(os.path.exists(FileName)):

        Ret = os.path.isabs(FileName)

        if(Ret == True):
            print("it is absulute path")
        
        else:
            print("it is relative path")
            NewPath = os.path.abspath(FileName)
            print("updated path : ",NewPath)
            
    else:
        print("there is no such file")

if __name__ == "__main__":  
    main()