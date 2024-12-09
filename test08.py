import pandas as pd
import numpy as np
from datetime import datetime
import csv
import requests

# File path
# input_file_path  = "D:/Politecnico/LM/Data and Information Quality/Project/movies.csv"
#url =  "https://github.com/lukamath/DIQ_Project/blob/master/movies.csv"
raw_url = "https://raw.githubusercontent.com/lukamath/DIQ_Project/master/movies.csv"
local_path = 'D:/Politecnico/LM/Data and Information Quality/Project/downloaded_file08.csv'
output_file_path = "D:/Politecnico/LM/Data and Information Quality/Project/cleaned_movies08.csv"
M_file_path= "D:/Politecnico/LM/Data and Information Quality/Project/M_ending_List08.csv"


# Download the file from the URL and save it locally
response = requests.get(raw_url)
if response.status_code == 200:
    with open(local_path, 'w', encoding='utf-8') as local_file:
        local_file.write(response.text)
else:
    raise Exception(f"Failed to download file. HTTP Status Code: {response.status_code}")

# Read the CSV file with headers
'''df = pd.read_csv(input_file_path, 
                       engine='python',
                       quoting=csv.QUOTE_NONE,  # Disable special handling for quotes
                       on_bad_lines='skip'      # Skip problematic rows
)'''

marker0 = ',";;;;;'  
marker1='M";;;;;'
marker2='"",,";;;;;'
marker_count=0
row_count = 0
exception_ending_count = 0
# M_list=[]

# Open the input file for reading and the output file for writing
with open(local_path, 'r', encoding='utf-8') as input_file, \
     open(output_file_path, 'w', encoding='utf-8') as output_file,\
     open(M_file_path, 'w', encoding='utf-8') as M_file:

    # Initialize a buffer for the current row
    current_row = []

    # Read the first line (header) and append it to current_row
    header_line = input_file.readline().strip()
    #current_row = [header_line]  # Initialize the buffer with the header
    output_file.write(header_line + '\n')

    # Read and process each line
    for line_number, line in enumerate(input_file, start=2):
        # if line_number==53: 
        #     print('13th char form righ is: ',line[-13])
        # Check if the last character of the line is a comma, or if there is a marker0 not attached to title 
        if ((len(line) >= 9 and marker0 in line and line[-9] != ')' and     \
            len(line) >= 9 and marker0 in line and line[-9] != ',') or      \
            (marker0 in line and len(line) < 8 )                    or      \
            marker1 in line or marker2 in line):

            if(line[-2]=='M'):
                M_line=line.strip()
                M_file.write(str(line_number) +  '{'+ M_line + + '\n')

            # Increment the marker count
            marker_count += 1       
            current_row.append(line.strip())
            output_file.write(','.join(current_row) + '\n')
            # output_file.write(str(current_row) + '\n')
            row_count += 1  # Increment the row count
            current_row = []  # Reset the buffer for the next row
        elif line.rstrip().endswith(',') or line.rstrip().endswith('M'):
            exception_ending_count += 1
            current_row.append(line.strip())
            output_file.write(','.join(current_row) + '\n')
            row_count += 1  # Increment the row count
            current_row = []  # Reset the buffer for the next row     
            
            if(line[-2]=='M'):
                M_line=line.strip()
                M_file.write(str(line_number) + '{'+ M_line + '}'+ '222222222222222'+'\n') 
                 
        else:
            # Add the line to the current row (stripping newline/extra spaces)
            current_row.append(line.strip())

            if(line[-2]=='M'):
                M_line=line.strip()
                M_file.write(str(line_number) + '{'+ M_line + '\n') 

    # Write any remaining data after the last marker
    if current_row:
        output_file.write(','.join(current_row) + '\n')
        row_count += 1
    


# Print summary
print(f"Total markers found: {marker_count}")
print(f"Total rows written: {row_count}")
# Print the comma ',' count
print(f"Number of lines ending with an exception (M or ,s): {exception_ending_count}")

