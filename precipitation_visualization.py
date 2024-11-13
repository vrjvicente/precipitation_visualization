from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

#A TEST

intro = ("This program shows a visual representation of precipitation "
         "in a given area from a user's CSV file.")
instruction = ("\nMake sure the CSV file is stored in the "
               "data folder.")

print(intro, instruction)

while True:
    file_name = input("\nPlease enter the CSV file you want to use for the data.\n"
                      "> ")
    file_name = file_name.removesuffix('.csv')
    path = Path(f'data/{file_name}.csv')

    try:
        lines = path.read_text(encoding='utf-8').splitlines()
    except FileNotFoundError:
        print(f"The file {file_name}.csv is not in the data folder.")
    else:
        break

location = input("Please enter the location of this data.\n"
                 "> ")
year = input("Please enter the year of this data.\n"
             "> ")

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    if column_header == 'DATE':
        date_index = index
    if column_header == 'PRCP':
        prcp_index = index

dates, prcps = [], []
for row in reader:
    current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
    try:
        prcp = float(row[prcp_index])
    except:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        prcps.append(prcp)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(dates, prcps, color='darkturquoise')

ax.set_title(f"Precipitation, {year}"
             f"\n{location}", fontsize=18)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Rainfall (mm)", fontsize=16)
ax.tick_params(labelsize=16)

while True:
    save_prompt = ("Would you like to save a copy of the figure? (y/n)\n"
                   "> ")
    save_answer = input(save_prompt)

    if save_answer.lower() == 'y':
        plt.savefig(f'figures/{file_name}.png', bbox_inches='tight')
        break
    elif save_answer.lower() == 'n':
        break
    else:
        print("Incorrect answer.")
        continue

plt.show()


