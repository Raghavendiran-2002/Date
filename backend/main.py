import os
from flask import Flask
import mysql.connector


class DBManager:
    def __init__(self, database='dyte', host="db", user="root", password_file=None):
        pf = open(password_file, 'r')
        self.connection = mysql.connector.connect(
            user=user,
            password=pf.read(),
            host=host,  # name of the mysql service as set in the docker compose file
            database=database,
            auth_plugin='mysql_native_password'
        )
        pf.close()
        self.cursor = self.connection.cursor()

    def populate_db(self):
        self.cursor.execute('DROP TABLE IF EXISTS log')
        self.cursor.execute(
            'CREATE TABLE log (id INT AUTO_INCREMENT PRIMARY KEY, message VARCHAR(255))')
        self.cursor.executemany('INSERT INTO log (id, message) VALUES (%s, %s);', [
                                (i, 'message log #%d' % i) for i in range(1, 5)])
        self.connection.commit()

    def query_titles(self):
        self.cursor.execute('SELECT message FROM log')
        rec = []
        for c in self.cursor:
            rec.append(c[0])
        return rec


server = Flask(__name__)
conn = None


@server.route('/')
def test():
    return "Started 🚀"


@server.route('/log-ingestor')
def logIngestor():
    # global conn
    # if not conn:
    #     conn = DBManager(password_file='/run/secrets/db-password')
    #     conn.populate_db()
    # rec = conn.query_titles()

    # response = ''
    # for c in rec:
    #     response = response + '<div>   Hello  ' + c + '</div>'
    return "Log Ingestor"


@server.route('/query-interface')
def queryInterface():
    return "Query Interface"


if __name__ == '__main__':
    server.run()
