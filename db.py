import sqlite3

class Db():

    def db_initiate(self, db_name, list):
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        connection.commit()
        connection.execute(""" CREATE TABLE TweetPulz (
            username text,
            tweet text
            )""")
        connection.execute(f"INSERT INTO TweePulz VALUES({list})")
        connection.commit()
