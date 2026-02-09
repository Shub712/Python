import sys
import os
import schedule
import time

#---------------------------------------------------------------
#
#   Function Name : CheckExtension
#   Description :   Used to Display Files With given Extension
#   Input :         Directory Name , Extension
#   Output :        File Names
#   Author :        Shubham Kiran Pawar
#   Date :          8.01.26
#
#---------------------------------------------------------------

def CheckExtension(Dirname,Extension):

    Border = "-"*45

    timestamp = time.ctime

    LogName = "Report.log"

    fobj = open(LogName,"w")
    fobj.write(Border+"\n")
    fobj.write("This is Log File Created By the Automation Script\n")
    fobj.write(Border+"\n")

    Ret = os.path.exists(Dirname)
    FileCount = 0

    if(Ret == False):
        print("Directory Doesnt exists")
        return
    
    Ret = os.path.isdir(Dirname)

    if(Ret == False):
        print("There is no such a directory")
        return
    
    for Folder,subfolder,files in os.walk(Dirname):
        for file in files:
            Name,Ext = os.path.splitext(file)
            FileCount = FileCount + 1
            if(Ext == Extension):
                print(file)
        fobj.write("The File Count is : "+str(FileCount)+"\n")

def main():

    Border = "-"*45

    print(Border)
    print("---------- Marvellous Automation ------------")
    print(Border)

    if(len(sys.argv)!= 3):

        print("Invalid commandline Argument")
        return
    
    CheckExtension(sys.argv[1],sys.argv[2])

    print(Border)
    print("---------- Marvellous Automation ------------")
    print(Border)

if __name__ =="__main__":
    main()