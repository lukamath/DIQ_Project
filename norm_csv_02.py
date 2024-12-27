import csv
import pandas as pd

# Input and output file paths
input_file_path = "moviesLM.csv"  # Replace with your input file path
output_file_path = "moviesLM_norm-02.csv"  # Replace with your desired output file path

# Open the input file for reading and the output file for writing
with open(input_file_path, "r", encoding="utf-8") as input_file, open(output_file_path, "w", encoding="utf-8", newline="") as output_file:
    # Use csv.reader to handle the input file
    reader = csv.reader(input_file, quotechar='"', delimiter=',', skipinitialspace=True,quoting=csv.QUOTE_MINIMAL)
    
    # Use csv.writer to write the normalized output
    writer = csv.writer(output_file)

    # Header normalization
    header = next(reader)
    writer.writerow(header)  # Write the header as-is

    # Process and write each row
    for row in reader:
        # Normalize and clean the row
        clean_row = [field.strip() if field else "" for field in row]
        writer.writerow(clean_row)

print(f"Normalized CSV saved to: {output_file_path}")

# Read the normalized CSV file into a DataFrame
df = pd.read_csv(output_file_path, encoding='utf-8')

# Display the first few rows to verify the data
print(df.head())

# Display information about the DataFrame
print("\nDataFrame Info:")
print(df.info())

print(df[['STARS','VOTES','RunTime','Gross']].head())

