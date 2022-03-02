from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
import datetime

stations = build_station_list()

update_water_levels(stations)
N = 5
highest_stations = stations_highest_rel_level(stations, N)

for j in highest_stations:
  station = j
  dt = 2
  degree = 4
  dates, levels = fetch_measure_levels(j.measure_id, dt = datetime.timedelta(days = dt))
  level_list = []
  for i in levels:
    if type(i) == list:
      x = i[1]
      level_list.append(x)
    else:
      level_list.append(i)

plot_water_level_with_fit(station, dates, level_list, degree)
