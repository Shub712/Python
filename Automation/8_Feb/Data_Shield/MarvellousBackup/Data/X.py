import os

def main():
    DirectoryName = input("Enter The Name Of Directory : ")

    print("Content of the directory are : ")

    for FolderName,SubFolderName,FileName in os.walk(DirectoryName):
        print("Folder Name : ",FolderName)

        for subf in SubFolderName:
            print("SubFolder Name : ", subf)

        for fname in FileName:
            print("File Name : ",fname)

if __name__ == "__main__":
    main()