
import psutil
import sys
import os
import time
import schedule

def CreateLog(FolderName):

    Ret = False

    Border = "-" *52

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)

        if(Ret == False):
            print("Unable to create directory")
            return

    else:
        os.mkdir(FolderName)
        print("Directory For Log Files Gets Created Successfully")
    
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    
    FileName = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)
    print("Log File gets created with name : ",FileName)

    fobj = open(FileName,"w")

    fobj.write(Border+"\n")
    fobj.write("------ Marvellous Platform Surveillance System -----\n")
    fobj.write("Log Created At : "+time.ctime()+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("----------------- System Report -------------------\n")

    #print("CPU Usage : ",psutil.cpu_percent())
    fobj.write("CPU usage : %s %%\n" %psutil.cpu_percent())
    fobj.write(Border+"\n")

    mem = psutil.virtual_memory()

    #print("RAM Usage : ",mem.percent)

    fobj.write("RAM Usage : %s %%\n" %mem.percent)
    fobj.write(Border+"\n")

    fobj.write("\nDisk Usage Report\n")
    fobj.write(Border+"\n")
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            #print(f"{part.mountpoint} used {usage.percent} %%")
            fobj.write("%s -> %s %% Used\n" %(part.mountpoint,usage.percent))
            
        except:
            pass

    fobj.write(Border+"\n")

    net = psutil.net_io_counters()

    fobj.write("Network Usage Report\n")
    fobj.write("Sent : %.2f MB\n" % (net.bytes_sent / (1024 * 1024)))
    fobj.write("Received : %.2f MB\n" % (net.bytes_recv / (1024 * 1024)))
    fobj.write(Border+"\n")

    #  Process Log

    fobj.write(Border+"\n")
    fobj.write("-------------------- END OF LOG FILE -------------------\n")
    fobj.write(Border+"\n")

def ProcessScan():
    print("Process Scan Report") 

    for proc in psutil.process_iter(attrs=["pid","name","status"]):
        info = proc.info
        print(info["pid"], info["name"], info["status"])                    # ps aux

def main():

    ProcessScan()
    return

    Border = "-" *52

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

        # Apply the schedular

        schedule.every(int(sys.argv[1])).minutes.do(CreateLog,sys.argv[2])

        print("Platform Surveillance System Started Successfully")
        print("Directory Created With Name : ", sys.argv[2])
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