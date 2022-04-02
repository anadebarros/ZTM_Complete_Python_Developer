import smtplib
from email.message import EmailMessage

email = EmailMessage()

email["from"] = "Ana de Barros"
email["to"] = "scralowrealow@gmail.com"
email["subject"] = "You've been hacked"

email.set_content("You are now under my command!")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("scralowrealow@gmail.com", "Goliasmanuel83")
    smtp.send_message(email)
    print("good")
