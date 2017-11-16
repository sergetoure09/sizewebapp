from db import *
import smtplib
from email.mime.text import MIMEText


class controlers:
    def __init__(self):
        print("Sarting app controler!")
        self.db_conn = Database()

    def record_entry_control(self, email, size):
        result = self.db_conn.record_entry_db(email, size)
        return result

    def send_data_email(self, email, size):
        print('sending email to... ', email)
        try:
            avg = self.db_conn.getavg()
            print(avg)
            from_email = "sergetoure.business@gmail.com"
            from_pwd = "Footballeur1985#$"
            to_email = email
            subject = "SizeApp auto-message"
            message = "hey there <br> Your height is <strong>{0}</strong><br> The average height is <strong>{1}</strong> ".format(size, avg)
            msg = MIMEText(message, 'html')
            msg['Subject'] = subject
            msg['From'] = from_email
            msg['To'] = to_email
            mailserver = smtplib.SMTP('smtp.gmail.com', 587)
            #print('voo')
            mailserver.ehlo()
           
            mailserver.starttls()
           
            mailserver.login(from_email, from_pwd)
            print('voo')
            mailserver.send_message(msg)
            print('email sent successfully to', email)
            return True
        except:
            print("error occured")
            return False
