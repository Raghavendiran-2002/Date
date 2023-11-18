import os
from flask import Flask, jsonify
import mysql.connector
import datetime
from flask import request
from flask_cors import CORS


class DBManager:
    def __init__(self, database='dyte', host="localhost", user="root", password="honda4104"):
        # pf = open(password_file, 'r')
        self.connection = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            database=database,
        )
        # pf.close()
        self.cursor = self.connection.cursor()

    def create_db(self):
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS log (level VARCHAR(25), message VARCHAR(255), resourceId VARCHAR(50), timestamp TIMESTAMP, traceId VARCHAR(30), spanId VARCHAR(30), commit VARCHAR(30), parentResourceId VARCHAR(40), FULLTEXT(level, message, resourceId,traceId,spanId,commit,parentResourceId));')
        # self.cursor.execute('ALTER TABLE log ADD FULLTEXT(message);')
        # self.cursor.execute('ALTER TABLE log ADD FULLTEXT(level);')
        # self.cursor.execute('ALTER TABLE log ADD FULLTEXT(message);')
        # self.cursor.execute('ALTER TABLE log ADD FULLTEXT(resourceId);')
        # self.cursor.execute('ALTER TABLE log ADD FULLTEXT(traceId);')
        # self.cursor.execute('ALTER TABLE log ADD FULLTEXT(spanId);')
        # self.cursor.execute('ALTER TABLE log ADD FULLTEXT(commit);')
        # self.cursor.execute('ALTER TABLE log ADD FULLTEXT(parentResourceId);')
        self.connection.commit()

    def insert_log(self, request_data):
        level = request_data['level']
        message = request_data['message']
        resourceId = request_data['resourceId']
        timestamp = datetime.datetime.strptime(
            request_data['timestamp'], "%Y-%m-%dT%H:%M:%S%fZ")
        traceId = request_data['traceId']
        spanId = request_data['spanId']
        commit = request_data['commit']
        parentResourceId = request_data['metadata']['parentResourceId']
        print("Working")
        print(type(timestamp))
        self.cursor.execute('INSERT INTO log (level, message , resourceId,timestamp,traceId,spanId,commit,parentResourceId) VALUES ("{0}", "{1}", "{2}","{3}", "{4}", "{5}", "{6}" , "{7}");'.format(
            level, message, resourceId, timestamp, traceId, spanId, commit, parentResourceId))
        self.connection.commit()

    def query_titles(self):
        self.cursor.execute('SELECT message FROM log;')
        rec = []
        for c in self.cursor:
            rec.append(c[0])
        return rec

    def search_level(self, level):
        self.cursor.execute(

            "SELECT * FROM log WHERE MATCH(level) AGAINST('{0}');".format(level))
        result = self.cursor.fetchall()
        return result
        # for x in result:
        # print(x)

    def search_message(self, message):
        self.cursor.execute(
            "SELECT * FROM log WHERE MATCH(message) AGAINST('{0}'); ".format(message))
        result = self.cursor.fetchall()
        return result

    def search_resourceId(self, resourceId):
        self.cursor.execute(
            "SELECT * FROM log WHERE MATCH(resourceId) AGAINST('{0}'); ".format(resourceId))
        result = self.cursor.fetchall()
        return result

    def search_timestamp(self, timestamp):
        self.cursor.execute(
            "SELECT * FROM log WHERE timestamp >= '2023-09-09' and timestamp < '2023-10-01';".format(timestamp))
        result = self.cursor.fetchall()
        return result

    def search_traceId(self, traceId):
        self.cursor.execute(
            "SELECT * FROM log WHERE MATCH(traceId) AGAINST('{0}'); ".format(traceId))
        result = self.cursor.fetchall()
        return result

    def search_spanId(self, traceId):
        self.cursor.execute(
            "SELECT * FROM log WHERE MATCH(spanId) AGAINST('{0}'); ".format(spanId))
        result = self.cursor.fetchall()
        return result

    def search_commit(self, commit):
        self.cursor.execute(
            "SELECT * FROM log WHERE MATCH(commit) AGAINST('{0}');".format(commit))
        result = self.cursor.fetchall()
        return result

    def search_parentResourceId(self, parentResourceId):
        self.cursor.execute(
            "SELECT * FROM log WHERE MATCH(parentResourceId) AGAINST('{0}'); ".format(parentResourceId))
        result = self.cursor.fetchall()
        return result


server = Flask(__name__)
CORS(server)
conn = None


@server.route('/')
def test():
    return "Started 🚀"


@server.route('/log-ingestor', methods=['POST'])
def logIngestor():
    request_data = request.get_json()
    global conn
    if not conn:
        conn = DBManager(password="honda4104")
        conn.create_db()
    conn.insert_log(request_data)
    print("********************* INSERTED *************************")
    return "Log Ingestor"


@server.route('/query-interface', methods=['GET'])
def queryInterface():
    global conn
    if not conn:
        conn = DBManager(password="honda4104")
    print(request.args.getlist("search")[0])
    if (request.args.getlist("search")[0] == ""):
        return {"status": 200, "message": "search field Empty"}
    if (request.args.getlist("filter")[0] == "level"):
        logs = conn.search_level(request.args.getlist("search")[0])
    if (request.args.getlist("filter")[0] == "message"):
        logs = conn.search_message(request.args.getlist("search")[0])
    if (request.args.getlist("filter")[0] == "resourceId"):
        logs = conn.search_resourceId(request.args.getlist("search")[0])
    if (request.args.getlist("filter")[0] == "timestamp"):
        logs = conn.search_timestamp(request.args.getlist("search")[0])
    if (request.args.getlist("filter")[0] == "traceId"):
        logs = conn.search_traceId(request.args.getlist("search")[0])
    if (request.args.getlist("filter")[0] == "spanId"):
        logs = conn.search_spanId(request.args.getlist("search")[0])
    if (request.args.getlist("filter")[0] == "commit"):
        logs = conn.search_commit(request.args.getlist("search")[0])
    if (request.args.getlist("filter")[0] == "parentResourceId"):
        logs = conn.search_parentResourceId(request.args.getlist("search")[0])
    response = {"status": 200, "logs": logs}
    return jsonify(response)


if __name__ == '__main__':
    server.run()
