from pathlib import Path
import csv

import generate_figure

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
        print("Was unable to find the precipitation data "
              "for that file.\n"
              "Please check the file for the precipitation (PRCP) "
              "and its date (DATE).")
    else:
        generate_figure.data_extract(reader, date_index, prcp_index,
                                     file_name)
        