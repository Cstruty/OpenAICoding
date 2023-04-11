import email, smtplib, ssl

# used for MMS
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from os.path import basename

def send_sms_via_email(
    number: str,
    message: str,
    subject: str = "sent using etext",
    smtp_server: str = "smtp.gmail.com",
    smtp_port: int = 465,
):
    sender_email="guelphbuscancellation@gmail.com"
    
    email_password="nvtxwqjtfivnxjvg"
    receiver_email = f'{number}@{"msg.telus.com"}'

    email_message = f"Subject:{subject}\nTo:{receiver_email}\n{message}"

    with smtplib.SMTP_SSL(
        smtp_server, smtp_port, context=ssl.create_default_context()
    ) as email:
        email.login(sender_email, email_password)
        email.sendmail(sender_email, receiver_email, email_message)


