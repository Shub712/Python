import sys
import os
import shutil
import time
def DirectoryCopyExt(Srcdir,Destdir,Extension):
    
    timestamp = time.ctime

    if not os.path.exists(Srcdir):
        print("Source File Does Not Exists")
        return
    
    if not os.path.isdir(Srcdir):
        print("Source File is not a directory")
        return

    if not os.path.isdir(Destdir):
        os.mkdir(Destdir)

    
    for Folder, Subfolder ,File in os.walk(Srcdir):
        for fname in File:
            src_path = os.path.join(Srcdir,fname)
            dest_path = os.path.join(Destdir,os.path.relpath(src_path,Srcdir))

            if(fname.endswith(Extension)):
                shutil.copy(src_path,dest_path)

def main():
    Border = "-"*40
    
    print(Border)
    print("----- Automation Script Is Running -----")
    print(Border)

    if len(sys.argv)!= 4:
        print("Invalid Commandline Arguement")
        print("Give Command As : Programname SourceFile DestinationFile Extenion")
        return
    
    DirectoryCopyExt(sys.argv[1],sys.argv[2],sys.argv[3])

    print(Border)
    print("------ Thank You For Using Script ------")
    print(Border)

if __name__ == "__main__":
    main()