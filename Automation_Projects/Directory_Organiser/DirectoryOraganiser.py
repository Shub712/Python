# -----------------------------------------------------------
#   Project Name : Directory Organiser
#   Description  : Sorts files based on extension
#   Author       : Shubham Kiran Pawar
#   Created On   : 10 Feb 2026
#   Version      : 1.0
# -----------------------------------------------------------


# -----------------------------------------------------------
#   Directory Organiser
#
#   Description:
#   This script scans a given directory and separates files
#   into folders based on their file extensions.
#
#   Example:
#   If the directory contains:
#       file1.txt
#       image.jpg
#       data.csv
#
#   It will create folders:
#       txt/
#       jpg/
#       csv/
#   And move files accordingly.
#
#   Usage:
#       python program.py DirectoryName
#
#   Optional:
#       --h  → Help
#       --u  → Usage
# -----------------------------------------------------------


import sys        # For accessing command-line arguments
import os         # For directory and file operations
import time       # For timestamps
import schedule   # For scheduling repeated execution
import shutil     # For moving files


# -----------------------------------------------------------
# Function Name : CreateLog
# Description   : Creates a log file and writes statistics
#                 about the directory organisation process.
# Input         : stats (dictionary containing counters)
# Output        : None
# -----------------------------------------------------------

def CreateLog(stats):

    # Generate safe timestamp for filename
    timestamp = time.strftime("%Y%m%d_%H%M%S")

    # Create log filename
    filename = f"Report_{timestamp}.log"

    border = "-" * 49

    # Creates Log File
    
    fobj = open(filename, "w") 

    fobj.write(border + "\n")
    fobj.write("----- Log File Created By Automation Script -----\n")
    fobj.write(f"Directories Made        : {stats['directories_made']}\n")
    fobj.write(f"Files With No Extension : {stats['noextension_files']}\n")
    fobj.write(f"Files Moved             : {stats['files_moved']}\n")
    fobj.write(border + "\n")
    fobj.close()

# -----------------------------------------------------------
# Function Name : DirectoryOrganiser
# Description   : Organises files inside a directory based
#                 on their file extensions.
# Input         : DirName (directory to be organised)
# Output        : stats (dictionary with operation counts)
# -----------------------------------------------------------
def DirectoryOrganiser(DirName):

    # Dictionary to store statistics
    stats = {
        "directories_made": 0,
        "files_moved": 0,
        "noextension_files": 0
    }

    # Check if path exists
    if not os.path.exists(DirName):
        print("There is no such directory.")
        return stats

    # Check if path is a directory
    if not os.path.isdir(DirName):
        print("Provided path is not a directory.")
        return stats

    # Walk through directory
    for Folder, SubFolder, Files in os.walk(DirName):

        # Process only files in root directory (not subfolders)
        if Folder != DirName:
            continue

        for fname in Files:

            # Full source path
            Source_Path = os.path.join(Folder, fname)

            # Split file name and extension
            name, ext = os.path.splitext(fname)

            # Determine folder name based on extension
            if ext == "":
                ext_folder = "NoExtension"
                stats["noextension_files"] += 1
                
            else:
                ext_folder = ext[1:]  # Remove dot from extension

            # Create destination directory path
            destination_dir = os.path.join(DirName, ext_folder)  # Ex - Demo/txt

            # Create directory if it does not exist
            if not os.path.exists(destination_dir):
                os.mkdir(destination_dir)
                stats["directories_made"] += 1

            # Destination file path
            destination_path = os.path.join(destination_dir, fname) # Exm- Demo/txt/A.txt

            # Move file
            shutil.move(Source_Path, destination_path)
            stats["files_moved"] += 1

    return stats


# -----------------------------------------------------------
# Function Name : job
# Description   : Wrapper function for scheduling.
#                 Calls organiser and logging.
# -----------------------------------------------------------
def job(Directory):

    stats = DirectoryOrganiser(Directory)

    # Create log only if files were moved
    if stats["files_moved"] > 0:
        CreateLog(stats)

# -----------------------------------------------------------
# Function Name : main
# Description   : Entry point of the program.
#                 Handles user input and scheduling.
# -----------------------------------------------------------
def main():

    Border = "-" * 53

    print(Border)
    print("----------- Welcome To Directory Organiser ----------")
    print(Border)
    print("\n")

    print("Script Started At :", time.ctime())

    # No arguments provided
    if len(sys.argv) == 1:
        print("No arguments provided.")
        print("Use --h for help or --u for usage.")
        return

    # One argument provided
    elif len(sys.argv) == 2:

        # Help option
        if sys.argv[1].lower() == "--h":
            print("This script sorts files based on their extensions.")
            print("It creates a new folder for each extension.")

        # Usage option
        elif sys.argv[1].lower() == "--u":
            print("Usage:")
            print("python program.py SourceDirectory")

        # Directory provided
        else:
            # Schedule job every 1 minute
            schedule.every(1).minutes.do(job, sys.argv[1])

            # Infinite loop to keep scheduler running
            while True:
                print("Checking directory...")
                schedule.run_pending()
                time.sleep(1)

    print("\nScript Ended At :", time.ctime())
    print(Border)
    print("---------- Thank You For Using Our Script -----------")
    print(Border)


# -----------------------------------------------------------
# Program execution starts here
# -----------------------------------------------------------
if __name__ == "__main__":
    main()


