import smtplib
import os
from email.message import EmailMessage

def send_email():
    email_address = os.environ.get('GMAIL_USERNAME')
    email_password = os.environ.get('GMAIL_PASSWORD')
    recipient = os.environ.get('RECIPIENT_1')

    msg = EmailMessage()
    msg['Subject'] = "Automated Report from GitHub"
    msg['From'] = email_address
    msg['To'] = recipient
    msg.set_content("Here is the automated update from your repo.")

    # Connect to Gmail SMTP
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)
        print("Email sent successfully!")

if __name__ == "__main__":
    send_email()
