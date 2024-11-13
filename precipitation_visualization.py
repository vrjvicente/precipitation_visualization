from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

def save_figure():
    while True:
        save_prompt = ("Would you like to save a copy of the figure? (y/n)\n"
                    "> ")
        save_answer = input(save_prompt).lower()

        if save_answer == 'y':
            plt.savefig(f'figures/{file_name}.png', bbox_inches='tight')
            break
        elif save_answer == 'n':
            break
        else:
            print("Incorrect answer.")

def visualization(dates, prcps, loc, year):
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(dates, prcps, color='darkturquoise')

    ax.set_title(f"Precipitation, {year}"
                f"\n{loc}", fontsize=18)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Rainfall (mm)", fontsize=16)
    ax.tick_params(labelsize=16)

    save_figure()
    plt.show()

def data_extract(reader):
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
    location = input("Please enter the location of this data.\n"
                        "> ")
    year = input("Please enter the year of this data.\n"
                    "> ")
    visualization(dates, prcps, location, year)

def collect_index(header, string):
    """Scans for the desired category and return its index."""
    for index, column_header in enumerate(header):
        if column_header == string:
            return index

intro = ("This program shows a visual representation of precipitation "
         "in a given area from a user's CSV file.")
instruction = ("\nMake sure the CSV file is stored in the "
               "data folder.")

print(intro, instruction)

file_name = input("\nPlease enter the CSV file you want to use for the data.\n"
                    "> ")
file_name = file_name.removesuffix('.csv')
path = Path(f'data/{file_name}.csv')

try:
    lines = path.read_text(encoding='utf-8').splitlines()
except FileNotFoundError:
    print(f"The file {file_name}.csv is not in the data folder.")
else:
    reader = csv.reader(lines)
    header_row = next(reader)

    date_index = collect_index(header_row, 'DATE')
    prcp_index = collect_index(header_row, 'PRCP')

    if not date_index or not prcp_index:
        print("Error")
    else:
        data_extract(reader)

        


