# Read the input file and process it
input_file = "data/cleaned.csv"
output_file = "data/final.csv"

with open(input_file, "r", encoding="utf-8") as infile:
    lines = infile.readlines()

# List to store the processed lines
processed_lines = []

for i in range(len(lines)):
    line = lines[i].strip()
    
    # If a line starts with a comma, it's a continuation of the previous line
    if line.startswith(","):
        processed_lines[-1] += line  # Append to the previous line
    else:
        # Otherwise, treat it as a new line
        processed_lines.append(line)

# Write the cleaned lines to the output file
with open(output_file, "w", encoding="utf-8") as outfile:
    for line in processed_lines:
        outfile.write(line + "\n")

print(f"File has been cleaned and saved to {output_file}")
