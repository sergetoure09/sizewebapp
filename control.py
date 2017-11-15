from db import *

class controlers:
    def __init__(self):
        print("Sarting app controler!")
        self.db_conn=Database()
        

    def record_entry_control(self,email,size):
        result=self.db_conn.record_entry_db(email,size)
        return result

    def send_data_email(self,email):
        print('sending email to ',email)

