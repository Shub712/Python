import os

def DirectoryScanner(DirectoryName = "Marvellous"):

    Ret = os.path.exists(DirectoryName)
    
    if(Ret == False):
        print("there is no such directory")
        return
    
    print("Content of the directory are : ")

    for FolderName,SubFolderName,FileName in os.walk(DirectoryName):        # 3 return values

        print("Folder Name : ",FolderName)

        for subf in SubFolderName:
            print("SubFolder Name : ", subf)

        for fname in FileName:
            print("File Name : ",fname)

def main():
    DirectoryName = input("Enter The Name Of Directory : ")
    
    DirectoryScanner(DirectoryName)

if __name__ == "__main__":
    main()