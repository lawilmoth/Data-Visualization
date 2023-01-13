import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'death_valley_temps.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        
        
        try:
            high = int(row[1])
            low = int(row[3])
            

        except ValueError:
            print(f"Missing data for the {current_date}")

        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

print(len(dates))
print(len(highs))

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')

ax.set_title("Daily High and Low Temps in Death Valley 2014", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis = "both", which = "major", labelsize=16)

plt.show()