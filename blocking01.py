import re
import requests

# URL of the file
file_path= "D:/Politecnico/LM/Data and Information Quality/DIQ_Project/movies.csv"

# Read the file content
with open(file_path, "r", encoding="utf-8") as file:
    input_text = file.read()

# Define the regex pattern
# Matches either marker0 or marker1 at the end of a line
pattern = r'(?:,";;;;;|M";;;;;)$'
# pattern = r'^(?!=.*(?:\)";;;;;|,,";;;;;)$)(?=.*(?:,";;;;;|M";;;;;|",,,))$'

# Use the regex to split into movie blocks
# `flags=re.MULTILINE` ensures the regex considers each line separately
movie_blocks = re.split(pattern, input_text, flags=re.MULTILINE)

# Clean and remove empty blocks
movie_blocks = [block.strip() for block in movie_blocks if block.strip()]

# # Print each block
# for i, block in enumerate(movie_blocks, 1):
#     print(f"Block {i}:")
#     print(block)
#     print("-" * 50)

# Save each block to a separate file
output_file_path = "D:/Politecnico/LM/Data and Information Quality/DIQ_Project/all_blocks.csv"  # Replace with the desired output folder path

# Write blocks to the output file with separators
with open(output_file_path, "w", encoding="utf-8") as output_file:
    for i, block in enumerate(movie_blocks, 1):
        output_file.write(f"Block {i}:\n")
        output_file.write(block)
        output_file.write("\n" + "-" * 50 + "\n")  # Add a separator between blocks

print(f"All blocks saved to: {output_file_path}")