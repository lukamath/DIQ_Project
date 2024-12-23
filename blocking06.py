import re

# URL of the file
file_path = "movies.csv"
# Read the file content
with open(file_path, "r", encoding="utf-8") as file:
    input_text = file.read()

# Define the regex pattern
#pattern = r'(?:^(?!.*\)).*,";;;;;|M";;;;;|",,,|^".*[0-9].*,+$|^".*\$.*M$)$'
pattern = r'^(?!.*\)).*,";;;;;|^.*,,";;;;;$|M";;;;;|",,,|^".*[0-9].*,+$|^".*\$.*M$'

# Use the regex to split into movie blocks
movie_blocks = re.split(pattern, input_text, flags=re.MULTILINE)

# Clean and remove empty blocks
movie_blocks = [block.strip() for block in movie_blocks if block.strip()]

# Save each block to a separate file
output_file_path = "all_blocks_v5.csv"

# Write blocks to the output file with separators
with open(output_file_path, "w", encoding="utf-8") as output_file:

    for i, block in enumerate(movie_blocks, 1):
        #output_file.write(f"Block {i}:\n")
        output_file.write(block)
        output_file.write("\n" + "-" * 50 + "\n")  # Add a separator between blocks

print(f"All blocks saved to: {output_file_path} - # of blocks: {i-1}")


norm1_file_path="norm1_file.csv"
# Open the input file for reading and the output file for writing
with open(output_file_path, 'r', encoding='utf-8') as input_file, \
     open(norm1_file_path, 'w', encoding='utf-8') as output_file:

    # Initialize a buffer and markers for the current row
    #current_row = []
    target_sequence = ", ;;;;;"
    replacement_char = "+"

    headers_line = input_file.readline().strip()  # Read the first line and remove trailing whitespaces
    output_file.write(headers_line)

    # Read and process all data lines
    for line_number, line in enumerate(input_file, start=2):
        if line.rstrip().endswith(target_sequence):
            line = line.rstrip().replace(target_sequence, replacement_char)
            output_file.write(line + "\n")
        else:
            output_file.write(line.strip()+"\n")

norm2_file_path="norm2_file.csv"
target_sequence_2 = '""";;;;;'
target_sequence_3 = ";;;;;"

with open(norm1_file_path, 'r', encoding='utf-8') as input_file, \
     open(norm2_file_path, 'w', encoding='utf-8') as output_file:
        # Read and process all data lines
    for line_number, line in enumerate(input_file, start=1):
        if line.rstrip().endswith(target_sequence_2):
            line = line.rstrip().replace(target_sequence_2, "")
            output_file.write(line.strip() + "\n")
        elif line.strip() == target_sequence_3:
            continue
        elif line.rstrip().endswith(target_sequence_3):
            line = line.rstrip().replace(target_sequence_3, "")
            output_file.write(line.strip() + "\n")
        else:
            output_file.write(line.strip()+"\n")
    
norm3_file_path="norm3_file.csv"
target_sequence_4='            ""'
target_sequence_5=', '
target_sequence_6='"'

with open(norm2_file_path, 'r', encoding='utf-8') as input_file, \
     open(norm3_file_path, 'w', encoding='utf-8') as output_file:
        # Read and process all data lines
    for line_number, line in enumerate(input_file, start=1):
        modified_line = line.replace(target_sequence_4, "")
        modified_line = modified_line.replace(target_sequence_5, "+")
        modified_line = modified_line.replace(target_sequence_6, "")
        output_file.write(modified_line.strip()+"\n")