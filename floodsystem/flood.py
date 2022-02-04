from floodsystem.station import MonitoringStation
from floodsystem.stationdata import update_water_levels
def stations_level_over_threshold(stations, tol):
    update_water_levels(stations)
    overrange_stations = []
    for station in stations :
        if station.typical_range_consistent() == True:
            if station.relative_water_level() > tol:
                level = station.relative_water_level()
                overrange_stations.append [station,level]
    return overrange_stations