from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number
stations = build_station_list()
rivers_with_at_least_one_station = rivers_with_station(stations)
print( len(rivers_with_at_least_one_station), 'stations')
l1 = list(rivers_with_at_least_one_station)
l1.sort(reverse = False)
l10 = l1[:10]
print (l10)

s = stations_by_river(stations)
cam = s['River Cam']
cam.sort()
print (cam)

