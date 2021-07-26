import requests
# import latlon
# import pandas as pd

def get_json(start,goal):
    headers = {'X-NCP-APIGW-API-KEY-ID': 'fau64bbv6v','X-NCP-APIGW-API-KEY':'mSF1qIX7C1medFNmQzRoy9qWaLgrcbYfn3uk8NTS'} 
    req = requests.get('https://naveropenapi.apigw.ntruss.com/map-direction/v1/driving?start='+start+'&goal='+goal+'&option=trafast', headers=headers) 
    req_js = req.json()
    return req_js

def path(req_js):
    path = []
    for i in req_js['route']['trafast'][0]['path']:
        path.append(i)
        # print(i)
    return path

def route_distance(req_js):
    route_distance = req_js['route']['trafast'][0]['summary']['distance']/1000
    return route_distance

def route_time(req_js):
    route_time = req_js['route']['trafast'][0]['summary']['duration']/60000
    return route_time
    


# 안산 - 경기 안산시 단원구 첨단로 670 37.29597094074058, 126.79451447053734
# 평택 - 경기 평택시 포승읍 원정리 1245-3 37.001767812955535, 126.81180429610909
# 화성 - 경기 화성시 향남읍 제약단지로 75 37.091030785108636, 126.91915718261635

# get_json = get_json("127.1058342,37.3597078","127.0759853,37.1794697")
# print(path(get_json)[-1])
# print(route_distance(get_json))
# print(route_time(get_json))
# start = ['126.79451447053734,37.29597094074058','126.81180429610909,37.001767812955535','126.91915718261635,37.091030785108636']
# distance = []
# time = []
# for j in start:
#     for i in latlon.list_station('data.csv'):
#         goal = str(i[2])+','+str(i[1])
#         startp = j
#         req_js = get_json(startp,goal)
#         distance.append(route_distance(req_js))
#         time.append(route_time(req_js))

