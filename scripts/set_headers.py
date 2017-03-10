import mysql.connector
from mitmproxy import ctx

class Replacer:
    def __init__(self, cnx, cursor):
        self.cnx, self.cursor = cnx, cursor

    def getUser(self, flow):
        if 'proxyauth' in flow.metadata: # TODO and user != None
            return flow.metadata['proxyauth'][0]
        else:
            return ""

    def isUser(self, flow):
        self.cursor.execute("SELECT * FROM User WHERE UserId='" + self.getUser(flow) + "';") # TODO make sure this doesnt include empty str
        row = self.cursor.fetchone ()
        return not (row is None)

    def createNewEntryForSite(self, userId, host):
        ctx.log("- Creating new site entry")
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
            return self.createNewEntryForSite(self.getUser(flow), host)
        else:
            return row[0]

    def getIdeaId(self, flow, hostId):
        self.cursor.execute("SELECT IdeaId FROM UserHost WHERE UserId='" + self.getUser(flow) + "' AND HostId=" + str(hostId) + ";")
        row = self.cursor.fetchone ()
        if (row is None):
            self.cursor.execute("INSERT INTO UserHost(UserId, HostId) VALUES ('" + self.getUser(flow) + "', " + str(hostId) + ");")
            self.cnx.commit()
            return self.cursor.lastrowid
        else:
            return row[0]

    def request(self, flow):
        ctx.log("Request recieved: " + flow.request.pretty_host + ". Metadata: " + str(flow.metadata))
        if not self.isUser(flow):
            ctx.log("- Not a user")
            return
        hostId = self.getHostId(flow)
        ideaId = self.getIdeaId(flow, hostId)
        flow.request.headers["x-idea-id"] = str(ideaId)

def start():
    cnx = mysql.connector.connect(user='root', password='Hello', database='test')
    cursor = cnx.cursor()
    return Replacer(cnx, cursor)

def done():
    self.cursor.close()
    self.cnx.close()
