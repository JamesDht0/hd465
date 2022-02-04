from floodsystem.geo import sorted_by_key
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import update_water_levels
def stations_level_over_threshold(stations, tol):
    update_water_levels(stations)
    overrange_stations = []
    for station in stations :
        if station.typical_range_consistent() == True :
            if station.relative_water_level() != None and station.relative_water_level() > tol:
                level = station.relative_water_level()
                overrange_stations.append ([station.name,level])
    return overrange_stations


def stations_highest_rel_level(stations, N):
    update_water_levels(stations)
    highest_N = []
    highest_N_s = []
    for station in stations :
        if station.typical_range_consistent() == True :
            if station.relative_water_level() != None :
                level = station.relative_water_level()
                highest_N.append ([station.name,level])
    highest_N_s = sorted_by_key(highest_N,1,reverse=True)
    return highest_N_s[:N]