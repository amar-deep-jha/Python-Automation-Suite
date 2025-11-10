# Email automation script
import smtplib, json, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

with open("config.json") as f:
    config = json.load(f)

sender = config["email"]["sender"]
password = config["email"]["password"]
receiver = config["email"]["receiver"]

msg = MIMEMultipart("alternative")
msg["Subject"] = "Automation Suite – Report"
msg["From"] = sender
msg["To"] = receiver
body = MIMEText("Automation Suite task completed successfully!", "plain")
msg.attach(body)

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.send_message(msg)
        print("✅ Email sent successfully!")
except Exception as e:
    print("❌ Error sending email:", e)
