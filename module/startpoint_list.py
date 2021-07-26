def startpoint_list(startpoint):
    idx = 0
    latlng = ['','']
    for i in startpoint:
        if i == ',':
            idx = 1
        if i.isnumeric() or i == '.':
            latlng[idx] += i
    latlng = list(map(float, latlng))

    # print(latlng)
    return latlng

# print(startpoint_list("(lat:37.5656068,lng:126.9812313)"))