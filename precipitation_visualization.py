from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

intro = ("This program shows a visual representation of precipitation "
               "in a given area from a user's CSV file.")
instruction = ("\nMake sure the CSV file is stored in the "
               "data folder.")

print(intro, instruction)

file_name = input("\nPlease enter the CSV file you want to use for the data.\n"
                  "> ")
file_name.removesuffix('.csv')

path = Path(f'data/{file_name}.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)