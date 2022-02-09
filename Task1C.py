from floodsystem.stationdata import build_station_list

def stations_within_radius(stations, centre, r):
  stationList = []
  stationDistanceList = stations_by_distance(stations, centre)
  for i in stationDistanceList:
    if i[1] < r:
      stationList.append(i[0])
  return stationList

stations = build_station_list()

stationList = stations_within_radius(stations, (52.2053, 0.1218), 10)

task1C = []
for i stationList:
  task1C.append(i.name)
  
task1C.sort()
print("The stations within 10km of Cambridge City Centre are: ", task1C)
