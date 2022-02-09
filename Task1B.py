from floodsystem.geo import stations_by_distance
from floodsytem.stationdata import build_station_list

stations = build_station_list()

stationDistanceList = stations_by_distance(stations, (52.2053, 0.1218))

task1B = []
for i in stationDistanceList:
    task1B.append((i[0].name, i[0].town, i[1]))

closestList = task1B[:10]
furthestList = task1B[-10:]

print("The 10 closest stations to Cambridge City Centre are: ", closestList)
print("The 10 furthest stations to Cambridge City Centre are: ", furthestList)
