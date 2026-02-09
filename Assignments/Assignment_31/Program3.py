import sys
import os
import time
import shutil

def CopyDirectory(Source,Destination):
    
    Border = "-"*45

    if not os.path.exists(Source):
        print(" Source Directory Does not exist")
        return
    
    if not os.path.isdir(Source):
        print("Source is not a directory")
        return
    
    if not os.path.isdir(Destination):
        os.mkdir(Destination)
    Count = 0
    for Folder,SubFolder,File in os.walk(Source):
        for fname in File:
            src_path = os.path.join(Folder,fname)
            dest_path = os.path.join(Destination,os.path.relpath(src_path,Source))
            shutil.copy(src_path,dest_path)
            Count = Count+1
    timestamp = time.ctime()

    fobj = open("Report.log","w")
    fobj.write(Border+"\n")
    fobj.write("---------- Automation Script Report ----------\n")
    fobj.write("Number of Files Copied : "+str(Count)+"\n")
    fobj.write("Files Gets Sucessfully Copied\n")
    fobj.write("------Thank You For Using Script -------")
    fobj.write(Border+"\n")
    
    #sobj.close()
    #fobj.close()

def main():

    Border = "-"*42

    print(Border)
    print("-------- Automation Script Running -------")
    print(Border)

    if len(sys.argv) < 3:
        print("Invalid Commmand line input")
        print("Please use --h for help")
        return
    
    if(len(sys.argv) != 3):

        print("Use Automation Scrpit as : ")
        print("Use command as : ProgramName.py SourceFile DestinationFile")
        print("SourceFile : The Folder You Want To Copy")
        print("DestinationFile : The Folder Name You want to paste the data in")
        
    CopyDirectory(sys.argv[1],sys.argv[2])

    print(Border)
    print("------ Thank You For Using Automation Script -------")
    print(Border)
        

    



if __name__ == "__main__":
    main()