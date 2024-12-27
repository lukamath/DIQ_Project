import csv
import pandas as pd

input_file_path = "movies.csv"  # Replace with your input file path

# Read the normalized CSV file into a DataFrame
df = pd.read_csv(input_file_path, encoding='utf-8')

# Clean up STARS column
df['STARS'] = df['STARS'].str.replace('\n', '').str.strip()
df['GENRE'] = df['GENRE'].str.replace('\n', '').str.strip()
# Display the first few rows to verify the data
print(df.head())

# Display information about the DataFrame
print("\nDataFrame Info:")
print(df.info())

# print(df[['STARS','VOTES','RunTime','Gross']].head())

# Check the result
print(df['STARS'].head())
print()
print(df['GENRE'].head())