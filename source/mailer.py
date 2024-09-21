from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from pathlib import Path
from smtplib import SMTP
from typing import Optional

from email.message import EmailMessage

def send_email(sender, recipient, subject, body):
    """A function that passes command line input into a message send to a server, to represent sending mail

    Args:
        sender (_type_): a string passed in from the command line that gives the name of the person sending the email
        recipient (_type_): A string passed in form the command line that gives the name of the person recieving the email
        subject (_type_): A shorter string that represents the subject line in the email
        body (_type_): A long string which represents the body text of the email
    """
    msg = MIMEMultipart("alternative")
    msg["From"] = sender
    msg["To"] = recipient
    msg["Date"] = formatdate(localtime=True)
    msg["Subject"] = subject

    if body is not None:
        msg.attach(MIMEText(body, "plain"))

    s = SMTP("localhost", 1025)
    s.sendmail(sender, recipient, msg.as_string())
    s.quit()