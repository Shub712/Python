#-----------------------------------------------------------
#   Data Shield
#-----------------------------------------------------------

import sys
import os
import time
import schedule
import shutil
import hashlib
import zipfile

def Make_Zip(Folder):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    zip_name = Folder +"_" + timestamp + ".zip"

    # Open The Zip File

    zobj = zipfile.ZipFile(zip_name,'w',zipfile.ZIP_DEFLATED)

    for root,dirs,files in os.walk(Folder):
        for file in files:
            full_path = os.path.join(root,file)
            relative = os.path.relpath(full_path,Folder)

            zobj.write(full_path,relative)

    zobj.close()

    return zip_name

def Calculate_hash(path):
    hobj = hashlib.md5()

    fobj = open(path,"rb")

    while True:
        data = fobj.read(1024)
        if not data:
            break
        else:
            hobj.update(data)

    fobj.close()

    return hobj.hexdigest()

def BackupFiles(Source,Destination):

    Copied_Files = []
    print("Creating The Backup Folder For Backup Process")

    os.makedirs(Destination, exist_ok=True)

    for root, dirs,files in os.walk(Source):
        for file in files:
            src_path = os.path.join(root,file)

            relativepath = os.path.relpath(src_path)

            dest_path = os.path.join(Destination,relativepath)

            os.makedirs(os.path.dirname(dest_path),exist_ok=True)

            #copy the files if its new
            if((not os.path.exists(dest_path))) or (Calculate_hash((src_path) != (dest_path))):
                shutil.copy2(src_path,dest_path)
                Copied_Files.append(relativepath)
                        
    return Copied_Files

def MarvellousDataShieldStart(Source = "Data"):

    Border = "-" *52
    BackupName = "MarvellousBackup"

    print(Border)
    print("Backup Process Started Sucessfully at : ",time.ctime())

    Files = BackupFiles(Source,BackupName)
    
    zip_file = Make_Zip(BackupName)

    print(Border)
    print("Backup Completed Sucessfully")
    print("Files Copied : ", len(Files))
    print("Zip File gets created : ",zip_file)
    print(Border)


def main():

    Border = "-" *52

    print(Border)
    print("------ Marvellous Data Shield System -----")
    print(Border)

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or (sys.argv[1] == "--H")):
            print("This Script is used to :")
            print("1 : Takes Automatic Backup At Given Time")
            print("2 : Backup Only New & Updated Files")
            print("3 : Create an Archive of Backup Periodically")

        elif(sys.argv[1] == "--u" or (sys.argv[1] == "--U")):
            print("Use The Automation Script as :")
            print("ScriptName.py TimeInterval SourceDirectory")
            print("TimeInterval : The Time in Minutes for periodic scheduling")
            print("SourceDirectory : Name of directory to be backed up")

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")
            
    # Python Demo.py 5 Data
    elif(len(sys.argv) == 3):
        print("Inside Projects logic")
        print("Time Interval : ", sys.argv[1])
        print("Directory name : ", sys.argv[2])

        # Apply the schedular

        schedule.every(int(sys.argv[1])).minutes.do(MarvellousDataShieldStart,sys.argv[2])

        print(Border)
        print("Data Shield System Started Successfully")
        print("Time interval in minutes: ", sys.argv[1])
        print("Press Ctrl + Z or Ctrl + C to stop the execution")
        print(Border)

        # Wait Till Abort
        while(True):
            schedule.run_pending()
            time.sleep(1)
    
    else:
        print("Invalid Number of command line arguements")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")

    print(Border)
    print("---------- Thank You For Using Our Script ----------")
    print(Border)


if __name__ == "__main__":
    main()