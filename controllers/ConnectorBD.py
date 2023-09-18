from time import sleep
import mysql.connector  

class Connector():
    def __init__(self):
        tries=0
        while tries<4:
            try:
                self.db = mysql.connector.connect(
                        host="172.18.0.2",
                        user="root",
                        passwd ="test123",
                        database = "boards_test"
                    )
                self.mycursor = self.db.cursor()
                return
            except:
                print("Could not connect to database. Retrying....")
                sleep(4)
            tries+=1
        print("ERROR:  Connection with DB has failed. Functions may not work as expected.")
