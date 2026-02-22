import sys
import os
import hashlib

def CheckSum(filename):
    
    fobj = open(filename,"rb")
    hobj = hashlib.md5()
    
    Buffer = fobj.read(1000)
    
    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)
    
    fobj.close()
    
    return hobj.hexdigest()
    

def DirectoryTravel(dir):
    
    if not (os.path.exists(dir)):
        print("Direct Not exists")
        return
    elif not (os.path.isdir(dir)):
        print("Directory with this name doesnt exists")
        return
    
    else:
        
        for Folder,Subfolder,File in os.walk(dir):
            
            for file in File:
                file = os.path.join(Folder,file)
                chksum = CheckSum(file)
                
                print(chksum)
                

def main():
    
    if(len(sys.argv) == 2):
        DirectoryTravel(sys.argv[1])
    
    else:
        print("Invalid CommandLine Input")
        return
         
if __name__ == "__main__":
    main()