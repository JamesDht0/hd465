import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import datetime
from floodsystem.analysis import polyfit

def plot_water_levels(station, dates, levels):
  plt.plot(dates, levels)
  if station.typical_range:
    low, high = station.typical_range
    plt.axhline(low, color='r', linestyle='--')
    plt.axhline(high, color='b', linestyle='--')
  plt.title(station.name)
  plt.xlabel('Date')
  plt.xticks(rotation=90)
  plt.ylabel('Water level')
  plt.tight_layout()
  plt.show()
  
def plot_water_level_with_fit(station, dates, levels, p):
  plt.plot(dates, levels)
  if station.typical_range:
    low, high = station.typical_range
    plt.axhline(low, color='r', linestyle='--')
    plt.axhline(high, color='b', linestyle='--')
  plt.title(station.name)
  plt.xlabel('Date')
  plt.xticks(rotation=90)
  plt.ylabel('Water level')
  poly, d0 = polyfit(dates, levels, p)
  date = date2num(dates)
  plt.plot(date, poly(date - d0))
  plt.tight_layout()
  plt.show()
