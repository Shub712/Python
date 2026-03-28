# ---------------------------------------------------------------
# Marvellous Data Shield System
# ---------------------------------------------------------------
# Author      : Shubham Pawar
# Created On  : 8 February
# Version     : 1.0
#
# Description :
# This automation script performs periodic backup of a given
# source directory. It copies only new or modified files using
# hash comparison and creates a compressed ZIP archive of the
# backup folder. A log file is also generated to track the
# backup activity.
#
# Features :
# 1. Incremental Backup (copies only new or modified files)
# 2. Automatic scheduling using time interval
# 3. ZIP archive creation of backup folder
# 4. Log file generation for backup records
# 5. Email notification with log file and backup archive
#
# Modules Used :
# sys        -> Command line argument handling
# os         -> File and directory operations
# time       -> Timestamp generation
# schedule   -> Task scheduling
# shutil     -> File copying utilities
# hashlib    -> File hash generation (MD5)
# zipfile    -> Creating ZIP archives
# smtplib    -> Sending email
# email      -> Email message formatting
# mimetypes  -> Detecting file types
#
# Usage :
# python ScriptName.py TimeInterval SourceDirectory
#
# Example :
# python DataShield.py 5 DataFolder
#
# This will run the backup every 5 minutes.
#
# ---------------------------------------------------------------
# ---------------------------------------------------------------
# Marvellous Data Shield System
#
# Description :
# This automation script performs periodic backup of a given
# source directory. It copies only new or modified files using
# hash comparison and creates a compressed ZIP archive of the
# backup folder. A log file is also generated to track the
# backup activity.
#
# Features :
# 1. Incremental Backup (copies only new or modified files)
# 2. Automatic scheduling using time interval
# 3. ZIP archive creation of backup folder
# 4. Log file generation for backup records
# ---------------------------------------------------------------


# Import required modules

import sys        # For command line arguments
import os         # For file and directory operations
import time       # For timestamps
import schedule   # For scheduling tasks automatically
import shutil     # For copying files
import hashlib    # For generating MD5 hash of files
import zipfile    # For creating ZIP archives
import smtplib    # For sending email
from email.message import EmailMessage
import mimetypes  # For identifying file types

# ---------------------------------------------------------------
# Function Name : RestoreBackup()
# Description   : Extract The Zip File
# Input         : Zip file path, And Folder Name
# Output        : NA
# Purpose       : Used to unpack the zip files in the Desired Folder
# ---------------------------------------------------------------

def RestoreBackup(Zip_file_path,Destination):
    shutil.unpack_archive(Zip_file_path,Destination)
    print(f"Unpacked Files into {Destination} Folder")

# ---------------------------------------------------------------
# Function Name : Send_mail()
# Description   : Sends an email with log file and ZIP backup
# Inputs        :
# Sender        -> Email ID of sender
# app_password  -> Gmail app password
# receiver      -> Receiver email ID
# subject       -> Email subject
# body          -> Email body
# log           -> Log file path
# zip           -> Backup ZIP file path
# ---------------------------------------------------------------
def Send_mail(Sender,app_password ,receiver,subject,body,log,zip):

    # Create email message object
    msg = EmailMessage()
    
    msg["From"] = Sender
    msg["To"] = receiver
    msg["Subject"] = subject
    
    # Set email body text
    msg.set_content(body)
    

    # ---------------- Attach Log File ----------------

    # Open log file in binary mode
    with open(log,'rb') as f :
        file_data = f.read()
        file_name = os.path.basename(log)
        
    # Detect mime type
    mime_type,_ = mimetypes.guess_type(log)
    
    # If mime type not detected use default
    if mime_type is None:
        mime_type = "application/octet-stream"
        
    mime_type, mime_subtype = mime_type.split('/')
        
    # Add log file as attachment
    msg.add_attachment(file_data,
                       maintype = mime_type,
                       subtype = mime_subtype,
                       filename = file_name)
    
    
    # ---------------- Attach ZIP Backup ----------------

    with open(zip,'rb') as z:
        file_data = z.read()
        file_name = os.path.basename(zip)
    
    mime_type, _ = mimetypes.guess_type(zip)
    
    if mime_type is None:
        mime_type = "application/octet-stream"
        
    mime_type, mime_subtype = mime_type.split('/')

    # Add zip file as attachment
    msg.add_attachment(file_data,
                       maintype = mime_type,
                       subtype = mime_subtype,
                       filename = file_name)
    
    
    # ---------------- Connect Gmail SMTP Server ----------------

    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)
    
    # Login using sender email and app password
    smtp.login(Sender,app_password) 
    
    # Send email
    smtp.send_message(msg)
    
    # Close SMTP connection
    smtp.quit()
    
    


# ---------------------------------------------------------------
# Function Name : make_zip()
# Description   : Creates a ZIP archive of the backup folder.
# Input         : folder -> Name of folder to compress
# Output        : Returns name of the created ZIP file
# ---------------------------------------------------------------
def make_zip(folder):

    # Create timestamp to make unique zip names
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    zip_name = folder+"_"+timestamp + ".zip"

    # Create zip object in write mode
    zobj = zipfile.ZipFile(zip_name,'w',zipfile.ZIP_DEFLATED)

    # Walk through all files in folder
    for root, dirs, files in os.walk(folder):
        for file in files:

            # Full path of file
            full_path = os.path.join(root,file)

            # Relative path inside zip
            relative = os.path.relpath(full_path,folder)

            # Add file to zip
            zobj.write(full_path,relative)
    
    # Close zip file
    zobj.close()

    return zip_name


# ---------------------------------------------------------------
# Function Name : calculate_hash()
# Description   : Calculates MD5 hash of a file
# Input         : path -> file path
# Output        : Returns hash value of the file
# Purpose       : Used to detect file changes
# ---------------------------------------------------------------
def calculate_hash(path):

    # Create MD5 hash object
    hobj = hashlib.md5()

    # Open file in binary mode
    fobj = open(path,"rb")

    # Read file in chunks of 1024 bytes
    while True :

        data = fobj.read(1024)

        if not data :
            break
        else:
            hobj.update(data)

    # Close file
    fobj.close()

    # Return final hash value
    return hobj.hexdigest()



# ---------------------------------------------------------------
# Function Name : BackupFiles()
# Description   : Copies new or modified files from source
#                 directory to backup directory
# Input         : Source      -> original folder
#                 Destination -> backup folder
# Output        : Returns list of copied files
# ---------------------------------------------------------------
def BackupFiles(Source , Destination):

    copied_files = []    

    print("Creating the backup folder for backup process")

    # Create backup directory if not present
    os.makedirs(Destination,exist_ok= True)

    # Traverse source directory
    for root, dirs, files in os.walk(Source):

        for file in files :

            src_path = os.path.join(root,file)

            # Maintain folder structure
            relative = os.path.relpath(src_path,Source)

            dest_path = os.path.join(Destination,relative)

            # Create required directory path
            os.makedirs(os.path.dirname(dest_path),  exist_ok= True)

            # Copy file if:
            # 1) File doesn't exist in backup
            # 2) File content has changed
            if((not os.path.exists(dest_path)) or (calculate_hash(src_path) != calculate_hash(dest_path))):

                shutil.copy2(src_path,dest_path)

                copied_files.append(relative)

    return copied_files


# ---------------------------------------------------------------
# Function Name : MarvellousDataShieldStart()
# Description   : Main backup process
# ---------------------------------------------------------------
def MarvellousDataShieldStart(Source):
    
    # Validate source directory
    if not os.path.exists(Source) and os.path.isdir(Source):
        print("The Directory Doesnt Exist")
        return
    
    Border = "-"*50
    BackupName = "BackupFolder"
    
    # Generate timestamp for log file
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    Logfilename = "Report"+timestamp+".log"
    
    # Open log file
    fobj= open(Logfilename,"w")

    fobj.write("Backup Start Time : "+timestamp+"\n")
    
    print(Border)
    print("Backup process started successfully at : ",time.ctime())
    print(Border)

    # Copy files to backup folder
    files = BackupFiles(Source,BackupName)
    
    # Create ZIP archive of backup
    zip_file = make_zip(BackupName)
    
    # Write copied files in log
    fobj.write("Copied Files Are : \n") 

    for f in files:
        fobj.write(f+"\n")
        
    fobj.write("Zip File Name : "+zip_file+"\n")

    # Close log file
    fobj.close()

    print(Border)
    print("Backup completed successfully")
    print("Files copied : ",len(files))
    print("Zip files gets created : ",zip_file)
    print(Border)
    
    # ---------------- Email Configuration ----------------

    sender_email = "sender@gmail.com"
    app_password = "###########"
    receiver_mail = "receiver@gmail.com"

    subject = "Report Of a Data Shield Script"

    body = ''' Good Afternoon,

        This mail contains the log file of the python automation script
        
        Regards
        Shubham 
        '''

    #Send mail with log and zip file
    
    Send_mail(sender_email,app_password,
            receiver_mail,subject,body,Logfilename,zip_file)



# ---------------------------------------------------------------
# Function Name : main()
# Description   : Entry point of the program
#                 Handles command line arguments
#                 and schedules backup process
# ---------------------------------------------------------------
def main():

    Border = "-"*50

    print(Border)
    print("--------- Marvellous Data Shield System ----------")
    print(Border)

    # If user passes only one argument
    if(len(sys.argv)== 2):

        # Help option
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):

            print("This script is used to : ")
            print("1 : Takes auto backup at given time ")
            print("2 : Backup only new and updated file")
            print("3 : Create an archive of the backup periodically")
            print("4 : Sends The Backup Zip and Log File through mail")
            print("5 : Unpacked The Zip File Created By Script")
            
        # Usage option
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):

            print("Use the automation script as")
            print("ScriptName.py TimeInterval SourceDirectory")

            print("TimeInterval : The time in minutes for periodic scheduling")

            print("SourceDirectory: Name of directory to be backed up")
            print("---------------------------------------------------")
            print("For Restore : program.py --restore Zipfilename Destination Folder name")
            print("---------------------------------------------------")


        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details")
    

    # If user provides interval and directory
    elif(len(sys.argv)== 3) :

        print("Inside projects logic")

        print("Time interval : ",sys.argv[1])

        print("Directory Name : ",sys.argv[2])
        
        # Schedule backup job
        schedule.every(int(sys.argv[1])).minutes.do(MarvellousDataShieldStart,sys.argv[2])

        print(Border)

        print("Data Shield System started successfully")

        print("Time interval in minutes : ",sys.argv[1])

        print("Press Ctrl + C to stop the execution")

        print(Border)
        
        # Infinite loop for scheduler
        while True :

            schedule.run_pending()

            time.sleep(1)
    elif(len(sys.argv)==4):
        if(sys.argv[1] == "--restore"):
            RestoreBackup(sys.argv[2],sys.argv[3])

    else:

        print("Invalid number of command line arguments")

        print("Unable to proceed as there is no such option")

        print("Please use --h or --u to get more details")
        

    print(Border)

    print("--------- Thank you for using our script ---------")

    print(Border)


# Program execution starts here
if __name__ =="__main__":

    main()