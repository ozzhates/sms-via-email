# SMS Sending Script

import smtplib

# Setup
email = '' # your email
pswd = '' # your email password
host = 'smtp.gmail.com' # SMTP server of your email provider
port = '587' # SMTP port

# Message and Recipient
    # This section has two modes: editing the info into the .py file, or using user input in shell
    # Make whichever one you don't want to use into a comment
# recipient = "" # who will receive the message. put this in email notation $$$$$$$$$$@txt.att.net
rcpt = input("What number do you want to send to? Include the email ending. Press enter when done. ")
# message = "" # what will be sent
msg = input("Input your message. Pressing enter will send it. ")

# Sending Process
server = smtplib.SMTP(host, port)
server.starttls()
server.login(email, pswd)
server.sendmail(email,rcpt,msg)
print('Message Sent')
server.quit()
