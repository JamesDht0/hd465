from .flood import stations_level_over_threshold
from .analysis import polyfit, find_gradient
from .datafetcher import fetch_measure_levels
import datetime

def stations_at_risk_of_flooding(stations):
  severeList = []
  highList = []
  moderateList = []
  lowList = []
  
  listOfStationTolerances = stations_level_over_threshold(stations, -10)
  for i in listOfStationTolerances:
    dates, levels = fetch_measure_levels(i[0].measure_id, dt = datetime.timedelta(hours = 6))
    if len(dates) > 10 and len(levels) > 10:
      level_list = []
      for j in levels:
        if type(j) == list:
          x = j[1]
          level_list.append(x)
        else:
          level_list.append(j)
      gradient = find_gradient(dates, level_list, 2)
      
      if i[1] >= 1.0:
        if gradient >= 0.0:
          severeList.append(i[0].town)
        elif gradient < 0.0:
          highList.append(i[0].town)
      elif i[1] >= 0.75 and i[1] < 1.0:
        if gradient >= 1.0:
          severeList.append(i[0].town)
        elif gradient > 0 and gradient < 1.0:
          highList.append(i[0].town)
        elif gradient <= 0:
          moderateList.append(i[0].town)
      elif i[1] >= 0.5 and i[1] < 0.75:
        if gradient >= 1.0:
          highList.append(i[0].town)
        elif gradient > 0 and gradient < 1.0:
          moderateList.append(i[0].town)
        elif gradient <= 0:
          lowList.append(i[0].town)
      elif i[1] >= 0.25 and i[1] < 0.5:
        if gradient >= 1.0:
          moderateList.append(i[0].town)
        else:
          lowList.append(i[0].town)
      else:
        lowList.append(i[0].town)
    else:
      pass
  return tuple([set(severeList), set(highList), set(moderateList), set(lowList)])
