from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

def save_figure():
    """Asks the user if they want a copy of the figure and if so, save
    the file.
    """
    while True:
        save_prompt = ("Would you like a copy of the figure?\n"
                       "> ")
        save_answer = input(save_prompt).lower()

        if save_answer == 'y' or save_answer == 'yes':
            plt.savefig(f'figures/{file_name}.png', bbox_inches='tight')
            print(f"\n---------- {file_name}.png has been saved in 'figures' "
                  "----------\n") 
            break
        elif save_answer == 'n' or save_answer == 'no':
            break
        else:
            print("\nInvalid answer. Please try again.")

def generate_figure(dates, prcps, loc, year):
    """Generates and views the figure using the given parameters."""
    plt.style.use('seaborn-v0_8')
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(dates, prcps, color='darkturquoise')

    ax.set_title(f"Precipitation from {year}"
                f"\n{loc}", fontsize=18)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("Rainfall (mm)", fontsize=16)
    ax.tick_params(labelsize=16)

    save_figure()
    print("\n---------- Currently viewing figure... ----------\n")
    plt.show()

def data_extract(reader):
    """Gathers the dates and precipitation from the CSV file and asks the
    user for the location and timeframe of the data.
    """
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
    year = input("Please enter the timeframe of this data.\n"
                 "> ")
    print()
    generate_figure(dates, prcps, location, year)

def collect_index(header, string):
    """Scans for the desired category and return its index."""
    for index, column_header in enumerate(header):
        if column_header == string:
            return index

print("---------------------------")
print("Precipitation Visualization")
print("---------------------------")

intro = ("This program displays a visual representation of precipitation "
         "in a given area from a CSV file.")
instruction = ("\nMake sure the CSV file is stored in the "
               "'./precipitation_visualization/data' folder.")

print(intro, instruction)

file_name = input("\nPlease enter the CSV file you want to use for the data.\n"
                  "> ")
file_name = file_name.removesuffix('.csv')
path = Path(f'data/{file_name}.csv')

try:
    lines = path.read_text(encoding='utf-8').splitlines()
except FileNotFoundError:
    print(f"\nThe file {file_name}.csv can not be found.\nPlease make "
          "sure that the file is in the folder and that the file is "
          "spelled correctly.")
else:
    reader = csv.reader(lines)
    header_row = next(reader)

    date_index = collect_index(header_row, 'DATE')
    prcp_index = collect_index(header_row, 'PRCP')

    print("\n---------- Collecting data... ----------\n")
    if not date_index or not prcp_index:
        print("\nWas unable to find the precipitation data "
              "for that file.\n"
              "Please check the file for the precipitation (PRCP) "
              "and its date (DATE).")
    else:
        data_extract(reader)
