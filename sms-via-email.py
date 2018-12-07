# SMS Sending Script

import smtplib

# Setup
email_host = 'smtp.gmail.com'
address = ''
port = '587'
password = ''

# Message and Recipient
    # This section has two modes: editing the info into the .py file, or using user input in shell
    # Make whichever one you don't want to use into a comment
# recipient = "" # who will receive the message. put this in email notation $$$$$$$$$$@txt.att.net
recipient = input("What number do you want to send to? Include the email ending.")
# message = "" # what will be sent
message = input("Message? ")

# Sending Process
server = smtplib.SMTP(email_host, port)
server.starttls()
server.login(address, password)
server.sendmail(address,recipient,message)
print("Message Sent")
server.quit()
