# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
def sorted_by_key(x, i, reverse=False):
    """For a list of lists/tuples, return list sorted by the ith
    component of the list/tuple, E.g.

    Sort on first entry of tuple:

      > sorted_by_key([(1, 2), (5, 1]), 0)
      >>> [(1, 2), (5, 1)]

    Sort on second entry of tuple:

      > sorted_by_key([(1, 2), (5, 1]), 1)
      >>> [(5, 1), (1, 2)]

    """

    # Sort by distance
    def key(element):
        return element[i]

    return sorted(x, key=key, reverse=reverse)


#from .utils import sorted_by_key  # noqa
def rivers_with_station(stations):
    #this function gives the set of rivers the input stations are along
    river_station = set()
    for station in stations:
        river_station.add (station.river)
    return river_station

def stations_by_river(stations):
    #this function gives the dictionary of stations along each river
    station_river = {}
    for station in stations:
        if station.river in station_river.keys():
            river = station_river[station.river]
            river.append (station.name)
            station_river.update({station.river : river})
        else:
            temp = list()
            temp.append(station.name)          
            station_river.update({station.river :temp})
    return station_river

def rivers_by_station_number(stations, N):
    unarranged_rivers = list()
    river_dict = stations_by_river(stations)
    for x in river_dict:
        river_tuple = (x , len(river_dict[x]))
        unarranged_rivers.append(river_tuple)
    arranged_rivers = sorted_by_key(unarranged_rivers,1,reverse=True)
    top_N=arranged_rivers[:10]
    print(top_N)
    n = N
    while arranged_rivers[n+1][1] == arranged_rivers[N][1]:
        top_N.append(arranged_rivers[n])
        n+=1
    return top_N
