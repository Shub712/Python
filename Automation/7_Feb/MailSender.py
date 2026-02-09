#=====================================================
#  Program    :   Marvellous_send_mail
#  Author     :   Shubham Kiran Pawar
#  Purpose    :   Send mail using Python  
#=====================================================

import smtplib
from email.message import EmailMessage

#--------------------------------------------
#  Function    :       Marvellous_send_mail
#  Description :       Sends email using Gmail SMTP server
#--------------------------------------------
def Marvellous_send_mail(sender,app_password,receiver,subject,body):

    # Step 1 : Create Email Object
    msg = EmailMessage()

    # Step 2 : Set email headers
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    # Step 3 : Add mail body
    msg.set_content(body)

    # Step 4 : Create SMTP SSL connection manually
    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    # Step 5 : Login using Gmail + App password
    smtp.login(sender,app_password)

    # Step 6 : Send the email
    smtp.send_message(msg)

    # Step 7 : Close connection manually
    smtp.quit()

#-------------------------------------
#  Function    :       main
#  Description :       Driver Code 
#-------------------------------------

def main():
    
    sender_email = "shubham.marvellousinfo@gmail.com" 
    app_password = "qsfi syfi iyys uhgb"

    receiver_email = "shubhamkiranpawar@gmail.com"

    subject = "Test Mail from Python Script"

    body = ''' Jay Ganesh .
    
    This is a test email sent using Marvellous Python.

    Regards,
    Marvellous Infosystems 
    '''

    Marvellous_send_mail(sender_email,app_password,receiver_email,subject,body)
    print("Marvellous Mail Sent Successfully")


#-------------------------------------
#   PROGRAM ENTRY POINT
#-------------------------------------

if __name__ == "__main__":
    main()