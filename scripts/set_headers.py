import mysql.connector

class Replacer:
    def __init__(self, cnx, cursor):
        self.cnx, self.cursor = cnx, cursor

    def request(self, flow):
        self.cursor.execute("SELECT IdeaId FROM UserHost WHERE UserId='laura' AND HostId=1;")
        row = self.cursor.fetchone ()
        flow.request.headers["x-idea-id"] = str(row[0])

def start():
    cnx = mysql.connector.connect(user='root', password='Hello', database='test')
    cursor = cnx.cursor()
    return Replacer(cnx, cursor)

def done():
    self.cursor.close()
    self.cnx.close()
