import sys
import os
import hashlib
import time
import schedule

def CheckSum(filename):
    
    fobj = open(filename,"rb")
    hobj = hashlib.md5()
    
    Buffer = fobj.read(1000)
    
    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1000)
    
    fobj.close()
    
    return hobj.hexdigest()
    

def FindDuplicate(dir):
    
    if not (os.path.exists(dir)):
        print("Direct Not exists")
        return
    
    elif not (os.path.isdir(dir)):
        print("Directory with this name doesnt exists")
        return    
    
    
    Duplicate = {}
        
    for Folder,Subfolder,File in os.walk(dir):
        
        for file in File:
            file = os.path.join(Folder,file)
            chksum = CheckSum(file)
            
            if chksum in Duplicate:
                Duplicate[chksum].append(file)
            else:
                Duplicate[chksum] = [file]

    DeleteDuplicate(Duplicate)
    
def DeleteDuplicate(Duplicate):
    
    
    timestamp = time.ctime()
    
    Logfilename = "Report%s.log"%timestamp
    Logfilename = Logfilename.replace(" ","_")
    Logfilename = Logfilename.replace(":","_")
    
    fobj = open(Logfilename,"w")
    
    for key,value in Duplicate.items():            
        if(len(value) > 1):
            fobj.write("Duplicate Deleted Files : \n")
            for file in value[1:]:
                fobj.write(file + "\n")
                os.remove(file)
                
            fobj.write("\n")
    
    fobj.close()
                           

def main():
    
    start_time = time.perf_counter()
    
    if(len(sys.argv) == 2):
        schedule.every(1).minute.do(FindDuplicate,sys.argv[1]) 
        
    
    else:
        print("Invalid CommandLine Input")
        return
    
    end_time = time.perf_counter()
    
    print(f"Execution Time : {end_time - start_time:.2f}Seconds")
    
    while True:
        schedule.run_pending()
        time.sleep(1)
    
         
if __name__ == "__main__":
    main()