import csv

input_file = 'sample.tsv'
output_file = 'output.tsv'

# Open input and output files
with open(input_file, mode='r', newline='', encoding='utf-8') as input_csv, open(output_file, mode='w', newline='') as output_csv:
    reader = csv.reader(input_csv, delimiter='\t')
    writer = csv.writer(output_csv, delimiter='\t')

    # Write the header row to the output file
    writer.writerow(['Item Name', 'Line Number'])

    # Process, filter, and sort rows
    filtered_and_sorted_rows = sorted(
        ((line_number, row[0]) for line_number, row in enumerate(reader, start=1) if row[0].startswith('Xerox')),
        key=lambda x: x[1]
    )

    # Write filtered and sorted rows to the output file
    for line_number, item_name in filtered_and_sorted_rows:
        writer.writerow([item_name, line_number])

# Output the contents of the output.tsv file
with open(output_file, mode='r') as output_csv:
    output_contents = output_csv.read()
    print(output_contents)

