'''
    Tarik Gusic 
    100 Yard Freestyle Project - Data Validation

    This code validates data -> checks data consistency and correctness
    

    Spreadsheet description:
      Place - int (in range 1 - 16)
      Time - double (SS.HH - two decimal spots)
      Year - date (YYYY - in range 2013-2024)
      University - string

'''
import pandas as pd
import os

# Set the current working directory to the location of the script
os.chdir(os.path.dirname(os.path.realpath(__file__)))

## Simple - reading the spreadsheet into DataFrames
df = pd.read_excel("top16_100free.xlsx", sheet_name="100 freestyle NCAA men", usecols="A:D")

# Check for empty cells
is_empty = df.isnull().values.any()
if is_empty:
    print(f'There are empty cells in the spreadsheet:\n{df.isnull().sum()}') # How many empty cells
else:
    print('No empty cells found in the spreadsheet!')


# Validate 'School' Column - Check for unique values
schools = df['School'].unique()
# Uncomment to inspect unique schools if needed
# print(sorted(schools))

# Validating 'Place' Column
errPlaceCol = False
for i in range(len(df['Place'])):
    if df['Place'].iloc[i] not in range(1,17): # Place is in range 1 to 16, inclusive
        print(f'Place Column - Error in row: {i+2}') # Tells where the mistake is
        errPlaceCol = True
if errPlaceCol is False: print("No Errors in Place Column!")

# Validating 'Time' Column
errTimeCol = False
for i in range(len(df['Time'])):
    time = str(df['Time'].iloc[i]).strip()
    # Check if the time matches the required format: two digits before and two after the decimal
    if not time.replace('.', '', 1).isdigit() or '.' not in time:
        # In case data isn't a number or has a decimal dot
        print(f'Time Column - Formatting error in row: {i+2}')
        errTimeCol = True
    elif len(time.split('.')[1]) > 2:
        # If there is more than two decimal spots of data
        ''' Note: when i put len(time.split('.')[1]) != 2 
        errors occur in field where the second decimal spot is 0
        '''
        print(f'Time Column - Decimal place error in row: {i+2}')
        errTimeCol = True
if errTimeCol is False : print('No Errors in Time Column!')


