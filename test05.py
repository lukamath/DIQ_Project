import pandas as pd
import numpy as np
from datetime import datetime
import csv

# File path
# input_file_path  = "D:/Politecnico/LM/Data and Information Quality/Project/movies.csv"
input_file_path  = "https://github.com/lukamath/DIQ_Project/blob/master/movies.csv"
output_file_path = "D:/Politecnico/LM/Data and Information Quality/Project/cleaned_movies05.csv"

# Read the CSV file with headers
df = pd.read_csv(input_file_path, 
                       engine='python',
                       quoting=csv.QUOTE_NONE,  # Disable special handling for quotes
                       on_bad_lines='skip'      # Skip problematic rows
)
marker0 = ',";;;;;'  
marker1='M";;;;;'
marker_count=0
row_count = 0
comma_ending_count = 0

# Open the input file for reading and the output file for writing
with open(input_file_path, 'r', encoding='utf-8') as input_file, \
     open(output_file_path, 'w', encoding='utf-8') as output_file:

    # Initialize a buffer for the current row
    current_row = []

    # Read and process each line
    for line_number, line in enumerate(input_file, start=1):
        # Check if the last character of the line is a comma
        if (len(line) >= 8 and marker0 in line and line[-8] != ')' or  (marker0 in line and len(line) < 8 ) or marker1 in line):
            # Increment the marker count
            marker_count += 1       
            current_row.append(line.strip())
            output_file.write(','.join(current_row) + '\n')
            # output_file.write(str(current_row) + '\n')
            row_count += 1  # Increment the row count
            current_row = []  # Reset the buffer for the next row
        elif line.rstrip().endswith(','):
            comma_ending_count += 1
            current_row.append(line.strip())
            output_file.write(','.join(current_row) + '\n')
            row_count += 1  # Increment the row count
            current_row = []  # Reset the buffer for the next row            
        else:
            # Add the line to the current row (stripping newline/extra spaces)
            current_row.append(line.strip())

    # Write any remaining data after the last marker
    if current_row:
        output_file.write(','.join(current_row) + '\n')
        row_count += 1

# Print summary
print(f"Total markers found: {marker_count}")
print(f"Total rows written: {row_count}")

# Print the coma ',' count
print(f"Number of lines ending with a comma: {comma_ending_count}")