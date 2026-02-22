#-----------------------------------------------------------
#   Data Shield
#-----------------------------------------------------------

import sys
import os
import time
import schedule
import shutil

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
            shutil.copy2(src_path,dest_path)

            Copied_Files.append(relativepath)
                        
    return Copied_Files

def MarvellousDataShieldStart(Source = "Data"):
    
    BackupName = "MarvellousBackup"

    print("Backup Process Started Sucessfully at : ",time.ctime())

    Files = BackupFiles(Source,BackupName)

    print("Report About The Backup")
    for name in Files:
        print(name)

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

        print("Data Shield System Started Successfully")
        print("Time interval in minutes: ", sys.argv[1])
        print("Press Ctrl + Z or Ctrl + C to stop the execution")

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