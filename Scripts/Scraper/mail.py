from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


class SendMail(object):
    def __init__(self):
        self.email = 'ohhalho@gmail.com'
        self.password = '13112766'
        self.server = 'smtp.gmail.com'
        self.port = 587

        self.recipients = 'mrpm1@globo.com'

        session = smtplib.SMTP(self.server, self.port)
        session.ehlo()
        session.starttls()
        session.login(self.email, self.password)
        self.session = session

    def send_message(self):
        message = MIMEMultipart("alternative")
        message["Subject"] = "Avengers: End Game"
        message["From"] = self.email
        message["To"] = self.recipients

        message.attach(MIMEText('Viadoooooo'))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(self.email, self.password)
            server.sendmail(self.email, message['To'].split(','), message.as_string())


if __name__ == '__main__':
    while True:
        SendMail().send_message()
        print('email seent')
