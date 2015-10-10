import pyorient
import sys
client = pyorient.OrientDB("localhost", 2424)
session_id = client.connect("root", "1111")
db_name = "soufun"
db_username = "admin"
db_password = "admin"
if client.db_exists( db_name, pyorient.STORAGE_TYPE_MEMORY ):
    client.db_open( db_name, db_username, db_password )
    print db_name + " opened successfully"
else:
    print "database [" + db_name + "] does not exist! session ending..."
    sys.exit()


lat1 = 22.533113
lat2 = 22.556300
lng1 = 114.038299
lng2 = 114.084304
query = 'SELECT FROM Listing WHERE latitude BETWEEN {} AND {} AND longitude BETWEEN {} AND {}'
records = client.command(query.format(lat1, lat2, lng1, lng2))
numListings = len(records)
print 'received ' + str(numListings) + ' records'
client.db_close()
record = records[0]
print type(record)

print record.price