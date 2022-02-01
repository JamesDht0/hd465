from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations
stations=build_station_list()
itrs = inconsistent_typical_range_stations(stations)
print(itrs)