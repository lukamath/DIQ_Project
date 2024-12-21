import re
import requests

# URL of the file
file_path = "movies.csv"
# Read the file content
with open(file_path, "r", encoding="utf-8") as file:
    input_text = file.read()

# Define the regex pattern
pattern = r'(?:^(?!.*\)).*,";;;;;|M";;;;;|",,,|^".*[0-9].*,+$|^".*\$.*M$)$'

# Use the regex to split into movie blocks
movie_blocks = re.split(pattern, input_text, flags=re.MULTILINE)

# Clean and remove empty blocks
movie_blocks = [block.strip() for block in movie_blocks if block.strip()]

# Save each block to a separate file
output_file_path = "all_blocks_x.csv"

# Write blocks to the output file with separators
with open(output_file_path, "w", encoding="utf-8") as output_file:
    for i, block in enumerate(movie_blocks, 1):
        output_file.write(f"Block {i}:\n")
        output_file.write(block)
        output_file.write("\n" + "-" * 50 + "\n")  # Add a separator between blocks

print(f"All blocks saved to: {output_file_path}")