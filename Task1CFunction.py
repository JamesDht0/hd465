#Outputting a list of stations within a distance r in km from a coordinate called centre).
def stations_within_radius(stations, centre, r):
  stationList = []
  stationDistanceList = stations_by_distance(stations, centre)
  for i in stationDistanceList:
    if i[1] < r:
      stationList.append(i[0])
  return stationList
