import psycopg2

class Database:
    mypath="dbname='testdb' user='sergetoure' password='Footballeur1985#$' host='127.0.0.1' port='5432'"
    def __init__(self):
        self.conn=psycopg2.connect(self.mypath)
        self.cur=self.conn.cursor()
        print("connection to database opened !\n You can start request")
    def __del__(self):
        self.conn.close()
        print("Connection to databsed closed !")
    def record_entry_db(self,email,size):
        try:
            self.cur.execute("INSERT INTO sizeapp VALUES (%s,%s)",(email,size))
        except Exception as e:
            print(e)

        