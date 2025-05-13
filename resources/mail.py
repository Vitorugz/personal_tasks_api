from smtplib import SMTP
import os

class Mail:
    def __init__(self):
        self.host = os.getenv('SMTP_HOST')
        self.port = os.getenv('SMTP_PORT')
        self.user = os.getenv('SMTP_USER')
        self.passwd = os.getenv('SMTP_PASSWD')

        self.smtp = SMTP(self.host, self.port)
        self.smtp.ehlo()
        self.smtp.starttls()
        self.smtp.login(self.user, self.passwd)

    def send(self, receiver, subject, body):
        self.smtp.sendmail(self.user, receiver, f"Subject: {subject}\n\n{body}")

        self.smtp.quit()