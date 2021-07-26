# import latlon
from haversine import haversine

# print(latlon.list_station())

def euclidian(startpoint, d_station):
    distance = []

    for i in d_station:
        start_lat = startpoint[0]
        start_lng = startpoint[1]
        dist = haversine((start_lat,start_lng),(i[1],i[2]))
        distance.append([dist,i[0],i[1],i[2]])

    return min(distance)

# d_station = latlon.list_station('test_latlong.csv')
# startpoint = [36.0855826, 128.36090520000002]
# print(euclidian(startpoint, d_station))
# print(euclidian([36.0855826, 128.36090520000002]))