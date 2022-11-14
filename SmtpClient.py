import sys
import smtplib
import email.utils
from email.mime.text import MIMEText


def getArguments():
    n = len(sys.argv)
    if n != 5:
        print("Input invalid.")
        print(sys.argv[1])
        sys.exit()

    else:
        sender = sys.argv[1]
        receiver = sys.argv[2]
        subject = sys.argv[3]
        messagepath = sys.argv[4]
        print("Sender: " + sender, "Receiver: " + receiver, "Subject: " + subject, "Message: " + messagepath)
        return sender, receiver, subject, messagepath


def readMessage(messagepath):
    try:
        with open(messagepath, 'r') as f:
            message = f.read()
            print(message)
            f.close()
            return message

    except IOError:
        print("Error: File does not appear to exist.")
        sys.exit()


def main():
    sender, receiver, subject, messagepath = getArguments()
    message = readMessage(messagepath)

    msg = MIMEText(message)
    msg['To'] = email.utils.formataddr(('Recipient', receiver))
    msg['From'] = email.utils.formataddr(('Author', sender))
    msg['Subject'] = subject

    server = smtplib.SMTP('127.0.0.1', 25)
    try:
        server.sendmail(sender, [receiver], msg.as_string())
    finally:
        server.quit()


main()
