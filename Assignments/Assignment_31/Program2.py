import sys
import os
import schedule
import time

def ExtensionReplace(Dirname,targetext,newext):
    
    if(not os.path.exists(Dirname) and not os.path.isdir(Dirname)):
        print("There is no such a directory exists")
        return
    
    for Folder,subfolder,file in os.walk(Dirname):
        for fname in file:
            if(fname.endswith(targetext)):

                oldfile = os.path.join(Folder,fname)
                newname = fname.replace(targetext,newext)
                newfile = os.path.join(Folder,newname)

                os.rename(oldfile,newfile)
                
                print(newfile)

def main():
    
    if(len(sys.argv) < 4):
        print("Invalid Command Line input is given")
        return
    
    ExtensionReplace(sys.argv[1],sys.argv[2],sys.argv[3])

if __name__ == "__main__":
    main()