from tkinter import *
import smtplib

root = Tk()

host = 'smtp.gmail.com' # SMTP server of your email provider
port = '587' # SMTP port
# Functions
def sending():
    email = e_email.get()
    pswd = e_pswd.get()
    rcpt = e_rcpt.get()
    msg = e_msg.get()
    server = smtplib.SMTP(host, port)
    server.starttls()
    server.login(email, pswd)
    server.sendmail(email,rcpt,msg)
    server.quit()
    e_msg.delete(0, 'end') # Clears message entry box

# Design
labelemail = Label(root, text="Email").grid(column=0, row=0, sticky=E)
e_email = Entry(root, bd =1)
e_email.grid(column=1, row=0)
labelpswd = Label(root, text="Password").grid(column=0, row=1, sticky=E)
e_pswd = Entry(root, bd =1, show='*')
e_pswd.grid(column=1, row=1)
labelrcpt = Label(root, text="Recipient").grid(column=0, row=2, sticky=E)
e_rcpt = Entry(root, bd =1)
e_rcpt.grid(column=1, row=2)
labelmsg = Label(root, text="Message").grid(column=0, row=3, sticky=E)
e_msg = Entry(root, bd =1)
e_msg.grid(column=1, row=3)
send = Button(root, text ="Send", command = sending, bd =1).grid(column=2, row=3)

root.title("sms-via-email")

root.mainloop()
