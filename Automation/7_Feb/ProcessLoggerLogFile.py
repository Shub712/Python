#----------------------------------------------
#   Creating Log File
#----------------------------------------------

import psutil
import sys
import os

def CreateLog(FolderName):

    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)

        if(Ret == False):
            print("Unable to create directory")
            return

    else:
        os.mkdir(FolderName)
        print("Directory For Log Files Gets Created Successfully")


def main():

    Border = "-"*52

    print(Border)
    print("------ Marvellous Platform Surveillance System -----")
    print(Border)

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or (sys.argv[1] == "--H")):
            print("This Script is used to :")
            print("1 : Create Automatic Logs")
            print("2 : Execute Periodically")
            print("3 : Sends mail with logs")
            print("4 : Stores information about processess")
            print("5 : Stores information about CPU")
            print("6 : Stores information about RAM usage")
            print("7 : Stores information about Secondary storage")
        
        elif(sys.argv[1] == "--u" or (sys.argv[1] == "--U")):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval DirectoryName")
            print("TimeInterval : The Time in Minutes for periodic scheduling")
            print("DirectoryName : Name of directory to create auto logs")

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")
            
    # Python Demo.py 5 Marvellous
    elif(len(sys.argv) == 3):
        print("Inside Projects logic")
        print("Time Interval : ", sys.argv[1])
        print("Directory name : ", sys.argv[2])

        CreateLog(sys.argv[2])
    
    else:
        print("Invalid Number of command line arguements")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")

    print(Border)
    print("---------- Thank You For Using Our Script ----------")
    print(Border)


if __name__ == "__main__":
    main()