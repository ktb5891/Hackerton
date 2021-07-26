from flask import Flask, render_template
from flask.globals import request
import latlon
import route
import startpoint_list
import euclidean
import find_addr

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def index():
    station_list = latlon.list_station('station_latlong.csv')
    startpoint = [37.465919,126.6338967]
    get_json = route.get_json("126.6338967,37.465919","126.9056849,37.4807199")
    path_list = route.path(get_json)
    route_distance = round(route.route_distance(get_json),3)
    route_time = round(route.route_time(get_json),3)
    startpoint_addr = find_addr.find_addr(startpoint)
    endpoint_addr = find_addr.find_addr((path_list[-1][1], path_list[-1][0]))
    return render_template('start_page.html', station_list = station_list, path_list = path_list, startpoint = startpoint, route_distance = route_distance, route_time = route_time, startpoint_addr = startpoint_addr, endpoint_addr = endpoint_addr)


@app.route('/select', methods=['POST','GET'])
def select():
    station_list = latlon.list_station('station_latlong.csv')
    startpoint = request.form['startpoint']
    # print(startpoint)
    startpoint = startpoint_list.startpoint_list(startpoint)
    min_station = euclidean.euclidian(startpoint,station_list)
    get_json = route.get_json(str(startpoint[1])+","+str(startpoint[0]),str(min_station[3])+","+str(min_station[2]))
    path_list = route.path(get_json)
    route_distance = round(route.route_distance(get_json),3)
    route_time = round(route.route_time(get_json),3)
    startpoint_addr = find_addr.find_addr(startpoint)
    endpoint_addr = find_addr.find_addr((path_list[-1][1], path_list[-1][0]))
    return render_template('start_page.html', station_list = station_list, path_list = path_list, startpoint = startpoint, route_distance = route_distance, route_time = route_time, startpoint_addr = startpoint_addr, endpoint_addr = endpoint_addr)

@app.route('/select2', methods=['POST','GET'])
def select2():
    station_list = latlon.list_station('station_latlong.csv')
    n_staion = latlon.list_station('profit_latlng.csv')
    station_list += n_staion
    startpoint = request.form['startpoint']
    # print(startpoint)
    startpoint = startpoint_list.startpoint_list(startpoint)
    min_station = euclidean.euclidian(startpoint,station_list)
    get_json = route.get_json(str(startpoint[1])+","+str(startpoint[0]),str(min_station[3])+","+str(min_station[2]))
    path_list = route.path(get_json)
    route_distance = round(route.route_distance(get_json),3)
    route_time = round(route.route_time(get_json),3)
    startpoint_addr = find_addr.find_addr(startpoint)
    endpoint_addr = find_addr.find_addr((path_list[-1][1], path_list[-1][0]))
    return render_template('start_page.html', station_list = station_list, path_list = path_list, startpoint = startpoint, route_distance = route_distance, route_time = route_time, startpoint_addr = startpoint_addr, endpoint_addr = endpoint_addr)


@app.route('/select3', methods=['POST','GET'])
def select3():
    station_list = latlon.list_station('station_latlong.csv')
    n_staion = latlon.list_station('leftout_latlng.csv')
    station_list += n_staion
    startpoint = request.form['startpoint']
    # print(startpoint)
    startpoint = startpoint_list.startpoint_list(startpoint)
    min_station = euclidean.euclidian(startpoint,station_list)
    get_json = route.get_json(str(startpoint[1])+","+str(startpoint[0]),str(min_station[3])+","+str(min_station[2]))
    path_list = route.path(get_json)
    route_distance = round(route.route_distance(get_json),3)
    route_time = round(route.route_time(get_json),3)
    startpoint_addr = find_addr.find_addr(startpoint)
    endpoint_addr = find_addr.find_addr((path_list[-1][1], path_list[-1][0]))
    return render_template('start_page.html', station_list = station_list, path_list = path_list, startpoint = startpoint, route_distance = route_distance, route_time = route_time, startpoint_addr = startpoint_addr, endpoint_addr = endpoint_addr)


app.run(host='127.0.0.1', port=8080, debug=True)