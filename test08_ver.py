import pandas as pd

# Define file paths
input_file_path = "D:/Politecnico/LM/Data and Information Quality/Project/cleaned_movies08.csv"
output_file_path= "D:/Politecnico/LM/Data and Information Quality/Project/cleaned_movies08_ver.csv"
valid_file_path = "D:/Politecnico/LM/Data and Information Quality/Project/valid_rows08.csv"
invalid_file_path = "D:/Politecnico/LM/Data and Information Quality/Project/invalid_rows08.csv" 



# Open the input file, process each line, and write to the output file
with open(input_file_path, 'r', encoding='utf-8') as infile, open(output_file_path, 'w', encoding='utf-8') as outfile:
    for line in infile:
        cleaned_line = line.replace(';;;;;,', '')  # Remove all occurrences of ';;;;;,'
        outfile.write(cleaned_line)

print(f"File cleaned and saved to {output_file_path}")



# Define the expected number of fields (columns)
expected_fields = 9  # correct number of columns

# Read the entire file as raw data
with open(input_file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Separate valid and invalid rows
valid_rows = []
invalid_rows = []

for line in lines:
    fields = line.strip().split(";;;;;,")  # Split by comma (adjust delimiter if needed)
    if len(fields) == expected_fields:
        valid_rows.append(fields)
    else:
        invalid_rows.append(fields)

# Convert valid rows into a DataFrame
df_valid = pd.DataFrame(valid_rows)

# Save valid rows to a CSV file
df_valid.to_csv(valid_file_path, index=False, header=False)
print(f"Valid rows saved to {valid_file_path}")

# Save invalid rows to another CSV file for review
with open(invalid_file_path, 'w', encoding='utf-8') as file:
    for row in invalid_rows:
        file.write(",".join(row) + "\n")
print(f"Invalid rows saved to {invalid_file_path}")
