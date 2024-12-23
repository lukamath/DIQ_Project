import csv

# Input CSV string (multiline)
csv_data = """A,B,C
aaa,"1,2,3,4","c1:
CCC
|c2:
CC1,
CC2,
CC3
"
"""

# Split the input data into lines
lines = csv_data.splitlines()

# Initialize storage for records
records = []
current_row = []
in_multiline_field = False  # Track if we are inside a multiline field

# Process each line
for line in lines:
    if in_multiline_field:
        # Append the line to the last field of the current row
        current_row[-1] += " " + line.strip()
        # Check if the multiline field ends
        if line.strip().endswith('"'):
            in_multiline_field = False  # End of multiline field
            records.append(current_row)  # Save the completed row
            current_row = []
    else:
        # Parse the line as comma-separated
        row = list(csv.reader([line], quotechar='"', delimiter=',', skipinitialspace=True))[0]
        if any(field.startswith('"') and not field.endswith('"') for field in row):
            # Start of a multiline field
            in_multiline_field = True
            current_row = row  # Save the start of the row
        else:
            # Normal row, save it directly
            records.append(row)

# Output the records
for record in records:
    print(record)
