import re
import requests

# URL of the file
file_path= "D:/Politecnico/LM/Data and Information Quality/DIQ_Project/block00.txt"

# Read the content of the file
with open(file_path, "r", encoding="utf-8") as file:
    input_text = file.read()    
# Define the pattern for splitting
pattern = r';;;;;(?=(?:[^"]*"[^"]*")*[^"]*$)'
movie_blocks = re.split(pattern, input_text)

# Clean and remove empty blocks
movie_blocks = [block.strip() for block in movie_blocks if block.strip()]

# Print each block
for i, block in enumerate(movie_blocks, 1):
    print(f"Block {i}:")
    print(block)
    print("-" * 50)
