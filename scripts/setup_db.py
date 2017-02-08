import mysql.connector

cnx = mysql.connector.connect(user='root', password='Hello',
                              database='test')
cursor = cnx.cursor()
# Drop tables
cursor.execute("DROP TABLE IF EXISTS UserHost;")
cursor.execute("DROP TABLE IF EXISTS Site;")
cursor.execute("DROP TABLE IF EXISTS User;")
cursor.execute("DROP TABLE IF EXISTS Host;")

# Setup tables
cursor.execute("CREATE TABLE User(UserId varchar(255), PRIMARY KEY (UserId));")
cursor.execute("CREATE TABLE Host(HostId int AUTO_INCREMENT, HostName varchar(255) UNIQUE, PRIMARY KEY (HostId));")
cursor.execute("CREATE TABLE Site(Url varchar(255), HostId int, PRIMARY KEY (Url), FOREIGN KEY (HostId) REFERENCES Host (HostId));")
cursor.execute("CREATE TABLE UserHost(IdeaId int AUTO_INCREMENT, UserId varchar(255), HostId int, UNIQUE (UserId, HostId), PRIMARY KEY (IdeaId), FOREIGN KEY (UserId) REFERENCES User(UserId), FOREIGN KEY (HostId) REFERENCES Host(HostId));")

# Populate tables
cursor.execute("INSERT INTO User (UserId) VALUES ('laura');")
cursor.execute("INSERT INTO User (UserId) VALUES ('calvin');")

cursor.execute("INSERT INTO Host (HostName) VALUES ('Google');")
cursor.execute("INSERT INTO Host (HostName) VALUES ('Youtube');")
cursor.execute("INSERT INTO Host (HostId) VALUES (0);") # Generates next id in sequence, w/o HostName
cursor.execute("INSERT INTO Host (HostId) VALUES (0);") # Generates next id in sequence, w/o HostName

cursor.execute("INSERT INTO Site (Url, HostId) VALUES ('google.com', 1);")
cursor.execute("INSERT INTO Site (Url, HostId) VALUES ('google.ie', 1);")
cursor.execute("INSERT INTO Site (Url, HostId) VALUES ('gmail.com', 1);")
cursor.execute("INSERT INTO Site (Url, HostId) VALUES ('youtube.com', 2);")
# cursor.execute("INSERT INTO Site (Url, HostId) VALUES ('infinite-wave-54273.herokuapp.com', 3);")
# cursor.execute("INSERT INTO Site (Url, HostId) VALUES ('localhost', 4);")

cursor.execute("INSERT INTO UserHost(UserId, HostId) VALUES ('laura', 1);")
cursor.execute("INSERT INTO UserHost(UserId, HostId) VALUES ('laura', 2);")
cursor.execute("INSERT INTO UserHost(UserId, HostId) VALUES ('laura', 3);")
cursor.execute("INSERT INTO UserHost(UserId, HostId) VALUES ('laura', 4);")
cursor.execute("INSERT INTO UserHost(UserId, HostId) VALUES ('calvin', 1);")

cnx.commit()

# Print
cursor.execute("SELECT * FROM User;")
table = cursor.fetchall()
print(table)

cursor.execute("SELECT * FROM Host;")
table = cursor.fetchall()
print(table)

cursor.execute("SELECT * FROM Site;")
table = cursor.fetchall()
print(table)

cursor.execute("SELECT * FROM UserHost;")
table = cursor.fetchall()
print(table)

cursor.close()
cnx.close()
