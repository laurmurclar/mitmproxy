import mysql.connector

class Replacer:
    def __init__(self, cnx, cursor):
        self.cnx, self.cursor = cnx, cursor

    def createNewEntryForSite(self, userId, host):
        # create new host
        self.cursor.execute("INSERT INTO Host (HostName) VALUES ('" + host + "');")
        newHostId = self.cursor.lastrowid
        # add site for host
        self.cursor.execute("INSERT INTO Site (Url, HostId) VALUES ('" + host + "', " + str(newHostId) + ");")
        # add user host
        self.cursor.execute("INSERT INTO UserHost(UserId, HostId) VALUES ('" + userId + "', " + str(newHostId) + ");")
        self.cnx.commit()
        return newHostId

    def getHostId(self, flow):
        host = flow.request.pretty_host
        self.cursor.execute("SELECT HostId FROM Site WHERE Url='" + host + "';")
        row = self.cursor.fetchone ()
        if (row is None):
            return self.createNewEntryForSite('laura', host)
        else:
            return row[0]

    def getIdeaId(self, userId, hostId):
        self.cursor.execute("SELECT IdeaId FROM UserHost WHERE UserId='" + userId + "' AND HostId=" + str(hostId) + ";")
        row = self.cursor.fetchone ()
        if (row is None):
            return -1   # should never happen (since should get added in getHostId)
        else:
            return row[0]

    def request(self, flow):
        hostId = self.getHostId(flow)
        ideaId = self.getIdeaId('laura', hostId)
        flow.request.headers["x-idea-id"] = str(ideaId)

def start():
    cnx = mysql.connector.connect(user='root', password='Hello', database='test')
    cursor = cnx.cursor()
    return Replacer(cnx, cursor)

def done():
    self.cursor.close()
    self.cnx.close()
