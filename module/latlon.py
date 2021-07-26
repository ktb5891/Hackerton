import pandas as pd

def list_station(file_route):
    #encoding = 'cp949'
    station = pd.read_csv(file_route, encoding='cp949')

    # print(station['주소'])
    d_station = []
    for i,j,k in zip(station['주소'],station['위도'],station['경도']):
        
        d_station.append([i ,j, k])

    return d_station
# file_route = 'test_latlong.csv'
# print(list_station(file_route))

# file_route = 'data.csv'
# print(list_station(file_route))