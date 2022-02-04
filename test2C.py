from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
stations = build_station_list()
top_10_relative = stations_highest_rel_level(stations,10)
print(top_10_relative)