# Precipitation Visualization
Generates a figure from a CSV file to show the amount of rainfall at a given location at a certain point in time.

## Requirements

### Matplotlib
```
import matplotlib
```

## How to Use

### Before the Program
Make sure that the CSV file is located in the `/data` directory.
- Weather files can be 

### Running the Program
1. Type in the file that is located in the 'data' directory. (Adding the `.csv` extension is optional.)
2. The program will ask for the location of the data and the timeframe.
3. The program will ask for if you would like to save the generated figure before viewing it.
    - The saved file will be located in the `/figures` directory.
  
## Troubleshooting

### The program was unable to find the file.
Error message:  `The file data.csv can not be found.`
- Check the '/data' folder and make sure that the file is in that folder.
- Make sure that the file is `.csv`.
- Make sure that the file name is typed correctly during prompt.

### The program was unable to gather the required information from the file.
Error message: `Was unable to find the precipitation data for that file.`\
\
The program looks into the first line of the file as the main header for `PRCP` and `DATE`. If one or both of the column names are missing,
the error message will occur.
- Check the CSV file and make sure that `PRCP` and `DATE` are included into the header and in its correct column.

## Development
