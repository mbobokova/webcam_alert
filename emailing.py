import smtplib
import filetype
from email.message import EmailMessage

# Connection settings
PASSWORD = "vdqk kaed irjp mhjl"
SENDER = "martina.bobokova@gmail.com"
RECEIVER = "martina.bobokova@gmail.com"
HOST = "smtp.gmail.com"


def send_email(img_path):
    print("send_email function started")

    # Email body
    email_message = EmailMessage()
    email_message["Subject"] = "New visitor came up"
    email_message.set_content("Someone arrived to yor object")

    # NEED TO FIGURE SUBTYPE
    with open(img_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=".png", filename=img_path)

    # Technical sending email
    gmail = smtplib.SMTP(HOST, 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()

    print("send_email function ended")


if __name__ == "__main__":
    send_email(img_path="images/1.png")


