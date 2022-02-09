#Calculating shortest distance of stations from a point p and outputting a sorted list of stations and their distances from p.
from haversine import haversine
def stations_by_distance(stations, p):
  stationDistanceList = []
  for i in stations:
    distance = haversine(i.coord, p)
    stationDistanceList.append(tuple([i, distance]))
    stationDistanceList.sort(key=lambda x: x[1])
  return stationDistanceList
