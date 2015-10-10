
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

totalPrice = 0
minPrice = 999999
maxPrice = 100

for record in records:
	print record.price
    
        totalPrice += record.price
        averagePrice = totalPrice / numListings

        if record.price < minPrice:
            minPrice = record.price

        if record.price > maxPrice:
            maxPrice = record.price

print 'min price: ' + str(minPrice)
print 'max price: ' + str(maxPrice)
print 'average price: ' + str(averagePrice)

client.db_close()