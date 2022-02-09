from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

stations = build_station_list()

stationList = stations_within_radius(stations, (52.2053, 0.1218), 10)

task1C = []
for i stationList:
  task1C.append(i.name)
  
task1C.sort()
print("The stations within 10km of Cambridge City Centre are: ", task1C)
