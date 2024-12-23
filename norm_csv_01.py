import csv

# Input and output file paths
input_file_path = "moviesLM.csv"  # Replace with your input file path
output_file_path = "moviesLM_norm-01.csv"  # Replace with your desired output file path


# Open the input file for reading and the output file for writing
with open(input_file_path, "r", encoding="utf-8") as input_file, open(output_file_path, "w", encoding="utf-8", newline="") as output_file:
    # Use csv.writer to write the cleaned output
    writer = csv.writer(output_file)

    # Buffer to reconstruct multiline fields
    reconstructed_row = []
    in_multiline_field = False  # Track if we're inside a multiline field

    for line in input_file:
        # Handle multiline fields
        if in_multiline_field:
            # Append the line to the last field in the reconstructed row
            reconstructed_row[-1] += " " + line.strip()
            # Check if the multiline field ends
            if line.strip().endswith('"'):
                in_multiline_field = False  # Multiline field ends
        else:
            # Parse the line into fields
            row = list(csv.reader([line], quotechar='"', delimiter=',', skipinitialspace=True))[0]
            
            # Check for the start of a multiline field
            for i, field in enumerate(row):
                if field.startswith('"') and not field.endswith('"'):
                    in_multiline_field = True  # Multiline field starts
                    reconstructed_row = row  # Start a new row
                    break
            else:
                # If no multiline field, write the row directly
                writer.writerow(row)

        # If the multiline field ends, write the reconstructed row
        if not in_multiline_field and reconstructed_row:
            # Clean and normalize multiline fields
            for i, field in enumerate(reconstructed_row):
                if field.startswith('"') and field.endswith('"'):
                    # Normalize multiline content within quotes
                    reconstructed_row[i] = " ".join(field.strip('"').splitlines()).replace(" | ", "|").strip()
            writer.writerow(reconstructed_row)
            reconstructed_row = []  # Reset for the next row

print(f"Normalized CSV saved to: {output_file_path}")
