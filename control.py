from db import *

class controlers:
    def __init__(self):
        self.db_conn=Database()
        print("Sarting app controler!")

    def record_entry_control(self,email,size):
        self.record_entry_db(self.email,self.size)

    #def send_data_email(email):
        #send email here

