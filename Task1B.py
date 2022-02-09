from haversine import haversine
def stations_by_distance(stations, p):
  stationDistanceList = []
  for i in stations:
    distance = haversine(i.coord, p)
    stationDistanceList.append(tuple([i, distance]))
    stationDistanceList.sort(key=lambda x: x[1])
  return stationDistanceList
