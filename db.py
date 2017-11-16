import psycopg2


class Database:
    #mypath = "dbname='sizeappDB' user='sergetoure' password='Footballeur1985#$' host='127.0.0.1' port='5432'"
    mypath = "dbname='d409e8q163vuf0' user='ahibkjttbrowzo' password='499eb20375ec377932e93c82cb420d7c8adcfe1fd6d9ad953cecb6598f0d1d2d' host='ec2-54-235-65-224.compute-1.amazonaws.com' port='5432'"
    def __init__(self):
        self.conn = psycopg2.connect(self.mypath)
        self.cur = self.conn.cursor()
        try:
            self.cur.execute('''CREATE  TABLE IF NOT EXISTS sizeapp (id SERIAL PRIMARY KEY,email TEXT,size INTEGER )''')
            self.conn.commit()
            print("connection to database opened ! You can start request")
        except Exception as e:
            print (e)
       

    def __del__(self):
        self.conn.close()
        print("Connection to database closed !")

    def getavg(self):
        self.cur.execute("SELECT size from sizeapp")
        data = self.cur.fetchall()
        f = list()
        for i in data:
            f.extend(list(i))
        avg = float(sum(f) / len(f))
        return avg

    def record_entry_db(self, email, size):
        print("Checking email in database...")
        self.cur.execute("SELECT email from sizeapp")
        data = self.cur.fetchall()
        f = list()
        for i in data:
            f.extend(list(i))
        if email in f:
            print("email found!")
            return False
        else:
            print("email not found we can proceed...")
            try:
                self.cur.execute("INSERT INTO sizeapp (email,size) VALUES (%s,%s)",
                                 (email, size))
                self.conn.commit()
                print("Entry recorded successfully!")
                return True
            except Exception as e:
                print(e)
                return False
