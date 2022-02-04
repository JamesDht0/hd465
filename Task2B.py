from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold
stations = build_station_list()
stations_over_08 = stations_level_over_threshold(stations,0.8)
print(stations_over_08)