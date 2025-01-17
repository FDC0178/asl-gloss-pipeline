import os

def process_file(input_file, output_file):
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            if line.startswith(","):
                # Retain the starting comma and remove others
                processed_line = "," + line[1:].replace(",", "")
            else:
                # Remove all commas if not starting with one
                processed_line = line.replace(",", "")
            outfile.write(processed_line)

# Example usage
input_file = "data/trainS.csv"             # Replace with your input file name
output_file = "data/cleaned.csv"     # Output file in the desired directory
process_file(input_file, output_file)

print(f"Processing complete. Check '{output_file}' for results.")
