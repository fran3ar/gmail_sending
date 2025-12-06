import smtplib
import os
import random # Imported to select a random item
from email.message import EmailMessage

def send_email():
    email_address = os.environ.get('GMAIL_USERNAME')
    email_password = os.environ.get('GMAIL_PASSWORD')
    recipient = os.environ.get('RECIPIENT_1')

    # 1. Define a list of emojis
    emojis = ["🚀", "📈", "✅", "🤖", "🔥", "📢", "✨", "📊", "🔔"]
    
    # 2. Pick one at random
    selected_emoji = random.choice(emojis)

    msg = EmailMessage()
    
    # 3. Insert the emoji into the subject using an f-string
    msg['Subject'] = f"{selected_emoji} Automated Report from GitHub"
    
    msg['From'] = email_address
    msg['To'] = recipient
    msg.set_content("Here is the automated update from your repo.")

    # Connect to Gmail SMTP
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)
        print(f"Email sent successfully with subject: {msg['Subject']}")

if __name__ == "__main__":
    send_email()
