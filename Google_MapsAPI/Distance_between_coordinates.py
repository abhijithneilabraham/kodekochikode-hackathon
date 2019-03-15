import googlemaps  
gmaps = googlemaps.Client(key='********************')  #API_Key
LatO = input("Origin Latitude :")
LongO = input("Origin Longitude :")
LatD = input("Destination Latitude :")
LongD = input("Destination Longitude :")
distance = gmaps.distance_matrix([str(LatO) + " " + str(LongO)], [str(LatD) + " " + str(LongD)], mode='walking')['rows'][0]['elements'][0]

print(distance["distance"]["text"])
