import googlemaps  
gmaps = googlemaps.Client(key='********************')   #API_Key  
origin_latitude = input("Origin Latitude :")
origin_longitude = input("Origin Longitude :")
destination_latitude = input("Destination Latitude :")
destination_longitude = input("Destination Longitude :")
distance = gmaps.distance_matrix([str(origin_latitude) + " " + str(origin_longitude)], [str(destination_latitude) + " " + str(destination_longitude)], mode='walking')['rows'][0]['elements'][0]

print(distance["distance"]["text"])
