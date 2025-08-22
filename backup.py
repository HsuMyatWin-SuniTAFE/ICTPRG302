from backupcfg import backupFile
from backupcfg import srcDir
from backupcfg import srcFile
from backupcfg import dstDir

import smtplib

import sys
import pathlib
import shutil
from datetime import datetime

import sys
import logging


#!/usr/bin/python3

"""
This Python code demonstrates the following features:

* send an email using the elasticemail.com smtp server.

"""



smtp = {"sender": "test20180818@gmail.com",    # elasticemail.com verified sender
        "recipient": "hwin@sunitafe.edu.au", # elasticemail.com verified recipient
        "server": "in-v3.mailjet.com",      # elasticemail.com SMTP server
        "port": 587,                           # elasticemail.com SMTP port
        "user": "7585eff6fa17564cbc044366f0405f8b",      # elasticemail.com user
        "password": "4b08502effb99a7469dc663dd01a165b"}     # elasticemail.com password

# append all error messages to email and send
def sendEmail(message):

    email = 'To: ' + smtp["recipient"] + '\n' + 'From: ' + smtp["sender"] + '\n' + 'Subject: Backup Error\n\n' + message + '\n'

    # connect to email server and send email
    try:
        smtp_server = smtplib.SMTP(smtp["server"], smtp["port"])
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.ehlo()
        smtp_server.login(smtp["user"], smtp["password"])
        smtp_server.sendmail(smtp["sender"], smtp["recipient"], email)
        smtp_server.close()
    except Exception as e:
        print(f"Exception occurs {e}")
        
#copy the file
def copyFileDirectory():
    """
    This Python code demonstrates the following features:
    
    * extracting the path component from a full file specification
    * copying a file
    * copying a directory.
    
    """
    try:
        dateTimeStamp = datetime.now().strftime("%Y%m%d-%H%M%S")  
        
        #srcFile = "/home/ec2-user/environment/ICTPRG302AssDoc/file1.txt"
        #srcDir = "/home/ec2-user/environment/ICTPRG302AssDoc/dir1"
        
        srcLoc = srcFile # change this srcLoc = srcDir to test copying a directory
        srcPath = pathlib.PurePath(srcLoc)
        
        #dstDir = "/home/ec2-user/environment/ICTPRG302AssDoc/backups"
        dstLoc = dstDir + "/" + srcPath.name + "-" + dateTimeStamp
        
        print("Date time stamp is " + dateTimeStamp) 
        print("Source file is " + srcFile)
        print("Source directory is " + srcDir)
        print("Source location is " + srcLoc)
        print("Destination directory is " + dstDir)
        print("Destination location is " + dstLoc)
        
        if pathlib.Path(srcLoc).is_dir():
            shutil.copytree(srcLoc, dstLoc) #copying the whole directory/folder
        else:
            shutil.copy2(srcLoc, dstLoc) #copying the file
    except Exception as e:
        sendEmail(f"Exception occurs {e}")
        print(f"Exception occurs {e}")
#!/usr/bin/python3

#check job number
#!/usr/bin/python3



logging.basicConfig(filename=backupFile, level=logging.DEBUG)
loggerFile = logging.getLogger()

def main():
    """
    This Python code demonstrates the following features:
    
    * accessing command line arguments.
    
    """
    try:
        argCount = len(sys.argv)
        program = sys.argv[0]
        arg1 = sys.argv[1] #getting job number. user provides the job number
        
        print("The program name is " + program + ".")
        print("The number of command line items is " + str(argCount) + ".")
        print("Command line argument 1 is " + arg1 + ".")
        if(arg1=='job1' or arg1 == 'job2' or arg1 == 'job3'): #check if job number is correct
            copyFileDirectory() # copy the file by calling "copyFileDirectory" function
            loggerFile.info("SUCCESS")
            print("copy the file")
        else:#if job number is incorrect
            print("logging and sending email")
            sendEmail("Job number is incorrect.") # sending email - error messsage
            loggerFile.error("Error - FAIL: job number incorrect") # logging error message
        
    except Exception as e:#catch the unexpected error
        sendEmail(f"Exception occurs {e}") #sending the email alert
        loggerFile.error("Execption occurs") #logging error
        print("ERROR - FAIL: An error occurred.")
    
if __name__ == "__main__":
    main()
    



    
#sending email alert -  Hsu will demonstrate -- will test in next week for sending email.
#creating backupcfg.py 
#logging every errors/exception


# HomeWork
# (1) What should be included in the backupcfg.py file? 
#     (e.g., source file path, log file path, backup destination, etc.)
# (2) Where should error handling and logging be added in the program? 
#     Think about: Where exceptions might occur
#     Where and how you should log those exceptions

