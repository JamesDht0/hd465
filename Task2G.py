from floodsystem.floodrisk import stations_at_risk_of_flooding
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
import datetime

stations = build_station_list()
update_water_levels(stations)

riskTowns = (stations_at_risk_of_flooding(stations))
print("The towns that are at severe risk are: ", riskTowns[0])
print("The towns that are at high risk are: ", riskTowns[1])
print("The towns that are at moderate risk are: ", riskTowns[2])
print("The towns that are at low risk are: ", riskTowns[3])
