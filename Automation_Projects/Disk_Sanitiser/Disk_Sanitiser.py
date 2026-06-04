# ---------------------------------------------------------------
# Project Name : Disk Sanitiser
# ---------------------------------------------------------------
# Author       : Shubham Pawar
# Created On   : 10/03/2026
# Version      : 1.0
#
# Description :
# This automation script scans a specified directory and
# identifies duplicate files using MD5 hash comparison.
# Files with identical content are considered duplicates.
# The script retains one copy of each file and removes the
# remaining duplicate copies automatically.
#
# Features :
# 1. Recursive directory traversal
# 2. MD5 checksum generation for file comparison
# 3. Duplicate file detection
# 4. Automatic duplicate file removal
# 5. Detailed deletion reporting
#
# Modules Used :
# os       -> File and directory operations
# hashlib  -> MD5 hash generation
#
# Usage :
# python DuplicateRemover.py
#
# Example :
# Enter Directory Name : DemoFolder
#
# ---------------------------------------------------------------

import hashlib
import os

# ---------------------------------------------------------------
# Function Name : CalculateChecksum()
# Description   : Generates MD5 checksum of a file.
# Input         : Filename -> Path of the file
# Output        : Returns MD5 hash string
# Purpose       : Used to compare file contents and identify
#                 duplicate files.
# ---------------------------------------------------------------

def CalculateChecksum(Filename):
    fobj = open(Filename,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1000)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()

# ---------------------------------------------------------------
# Function Name : FindDuplicate()
# Description   : Traverses the specified directory and finds
#                 duplicate files using MD5 hash comparison.
# Input         : DirectoryName -> Directory to scan
# Output        : Dictionary containing checksum as key and
#                 list of files having the same checksum.
# Purpose       : Identifies duplicate files based on content.
# ----------------------------------------------------------------

def FindDuplicate(DirectoryName= "Marvellous"):
    Ret = False

    Ret = os.path.exists(DirectoryName)
    if(Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirectoryName)
    if(Ret == False):
        print("It is not a directory")
        return
    
    Duplicate = {}
    
    for FolderName,SubFolderName, FileName in os.walk(DirectoryName):

        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            Checksum = CalculateChecksum(fname)

            if Checksum in Duplicate:
                Duplicate[Checksum].append(fname)
            else:
                Duplicate[Checksum] = [fname]
        
    return Duplicate    

# ---------------------------------------------------------------
# Function Name : DeleteDuplicate()
# Description   : Deletes duplicate files from the specified
#                 directory while keeping one original copy.
# Input         : Path -> Directory path
# Output        : Displays deleted files count
# Purpose       : Removes redundant duplicate files and frees
#                 storage space.
# ---------------------------------------------------------------

def DeleteDuplicate(Path = "Marvellous"):
    MyDict = FindDuplicate(Path)

    Result = list(filter(lambda x : len(x) > 1 , MyDict.values()))

    Count  = 0 
    Cnt = 0

    for value in Result:
        for subvalue in value:
            Count = Count + 1
            if(Count>1):
                print("Deleted file : ",subvalue)
                os.remove(subvalue)
                Cnt = Cnt + 1
        Count = 0

    print("Total deleted files : ",Cnt)
    
# ---------------------------------------------------------------
# Function Name : main()
# Description   : Entry point of the application.
#                 Accepts directory name from the user and
#                 initiates duplicate file removal process.
# Input         : User input (Directory Name)
# Output        : Displays deletion status and summary.
# Purpose       : Controls program execution flow.
# ---------------------------------------------------------------
def main():
    
    DirectoryName = input("Enter Directory Name : ")

    DeleteDuplicate(DirectoryName)

if __name__ =="__main__":
    main()