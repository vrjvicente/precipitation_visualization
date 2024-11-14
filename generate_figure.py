from datetime import datetime

import matplotlib.pyplot as plt

def save_figure(file_name):
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

def generate_figure(dates, prcps, loc, year, file):
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

    save_figure(file)
    print("\n---------- Currently viewing figure... ----------\n")
    plt.show()

def data_extract(reader, date_i, prcp_i, file):
    """Gathers the dates and precipitation from the CSV file and asks the
    user for the location and timeframe of the data.
    """
    dates, prcps = [], []
    for row in reader:
        current_date = datetime.strptime(row[date_i], '%Y-%m-%d')
        try:
            prcp = float(row[prcp_i])
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
    generate_figure(dates, prcps, location, year, file)