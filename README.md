# sms-via-email
Send SMS messages to people using an SMTP email server
## WARNING: THIS MAY CAUSE THE RECIPIENT TO HAVE TO PAY SMS/MMS FEES
## What it does
- Logs into your email using SMTP
- Uses the email to send a message to a phone number. [Learn more about what this is](https://www.att.com/esupport/article.html#!/wireless/KM1061254)

## How to run it
##### For CLI:
After you set it up, run `python sms-via-email.py`. Then follow the prompts

##### For GUI:
For non-gmail email addresses, edit the `host` and `port` values according to "Email SMTP Servers and Ports" below. In CMD/terminal, run `python GUI.py`. A window will appear. In this window, enter the info asked. Press "Send"

## How to set it up
- For "email", enter your whole email address
- For "pswd", enter the password for your email address
- For "host", enter the SMTP server for your email provider (This is set up for Gmail)
- For "port", enter the SMTP port (This is typically 587)
- For "rcpt", enter the phone number of the person to receive the message followed by the email suffix of their cell phone provider. Find their service provider using https://freecarrierlookup.com/
- For "msg", enter what you want the recipient to see
- If you have Gmail, go [here](https://www.google.com/settings/security/lesssecureapps) and turn the setting on

## Recipient and message options
Recipient and message have two ways that they can be input. One way involves editing the .py file and inserting the info. The second way (set as default) involves reading what you type after you run the .py file.

In order to switch to a different option, you can remove the `#` in front of the line. Add a `#` to the front of the one you want to turn off. Do not have two recipient lines or two message lines. This will break the program.

###### Email SMTP Servers and Ports
| Email Provider | SMTP Server | Port |
| :- | :- | :-: |
| Gmail | smtp.gmail.com | 587 |
| ATT | smtp.mail.att.net | 587 |
| Comcast | smtp.comcast.net | 587 |
| Yahoo | smtp.mail.yahoo.com | 587 |
| Outlook | smtp-mail.outlook.com | 587 |

###### Phone SMS and MMS suffixes
Using the SMS one is faster, but the MMS one allows a second message to stay in the same "conversation" on their end.

| Service Provider | SMS Suffix | MMS Suffix |
| :- | :- | :-: |
| AT&T | @txt.att.net | @mms.att.net |
| Sprint | @messaging.sprintpcs.com | @pm.sprint.com |
| Verizon | @vtext.com | @vzwpix.com |
| T-Mobile | @tmomail.net | @tmomail.net |
