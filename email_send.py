from html.entities import html5
from multiprocessing.spawn import prepare
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



class Email:
    def __init__(self,from_email,to_email,
                subject,html_code,text,
                host):
        self.from_email = from_email
        self.to_email = to_email
        self.subject = subject
        self.html_code = html_code 
        self.text = text  
        self.server = host
 

    def prepare_template(self):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = self.subject
        msg['From'] = self.from_email
        msg['To'] = self.to_email

        # Record the MIME types of both parts - text/plain and text/html.
        part1 = MIMEText(self.text, 'plain')
        part2 = MIMEText(self.html_code, 'html')
        msg.attach(part1)
        msg.attach(part2)
        return msg

    def send_mail(self,user_name,password):
        msg = self.prepare_template()
        if self.server == "local_host":
            s = smtplib.SMTP('localhost')
            # sendmail function takes 3 arguments: sender's address, recipient's address
            # and message to send - here it is sent as one string.
            s.sendmail(self.from_email, self.to_email, msg.as_string())
            s.quit()

        else:
            # Send the message via local SMTP server.
            mail = smtplib.SMTP('smtp.gmail.com', 587)
            mail.ehlo()
            mail.starttls()
            mail.login(user_name, password)
            s.sendmail(self.from_email, self.to_email, msg.as_string())
            mail.quit()





