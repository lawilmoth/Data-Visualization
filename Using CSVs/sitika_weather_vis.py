import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = "Using CSVs/sitka_weather.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    


    dates, highs = [], [] ######
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')####
        dates.append(current_date)######
        high = int(row[5])
        highs.append(high)



plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red') ####

#Format the graph
ax.set_title("Daily High Temps 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Temperature (F)', fontsize=16)
fig.autofmt_xdate()####
ax.tick_params(axis='both', which ='major', labelsize = 16)

plt.show()