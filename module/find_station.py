import geopy
import pandas as pd
import csv

def load_station():
    station = pd.read_csv('C:/Users/ktb58/OneDrive/바탕 화면/해커톤/Web_project/dataset/suso_station.csv', encoding='cp949')
    # print(station['주소'])
    service = geopy.Nominatim(user_agent = "myGeocoder")  
    # Nominatim 서비스 객체에 대한 핸들러 가져 오기
    d_station = {}
    f = open('station_latlong.csv','w', newline='')
    wr = csv.writer(f)
    for stat,loca in zip(list(station['충전소']),list(station['주소'])):
        service = geopy.Nominatim(user_agent = "myGeocoder")
        locationObj = service.geocode(loca)
        s_lat = locationObj.latitude
        s_long = locationObj.longitude
        d_station[stat]=  (s_lat,s_long)
        print(loca)
        
        wr.writerow([loca,s_lat,s_long])
        
    f.close()
    return d_station

# load_station()
# print(d_station)
# station = pd.read_csv('C:/Users/ktb58/OneDrive/바탕 화면/해커톤/Web_project/dataset/suso_station.csv', encoding='cp949')
# print(station.tail())