import csv
# specify the input and output file paths
input_file = 'gene_data.csv'
output_file = 'output.csv'
# specify the search value
search_value = 'A05'
# open the input file for reading and the output file for writing
with open(input_file, 'r') as f_in, open(output_file, 'w', newline='') as f_out:
    # create a CSV reader and writer objects
    reader = csv.reader(f_in)
    writer = csv.writer(f_out)
    # iterate over each row in the input file
    for row in reader:
        # check if the search value is in the current row
        if search_value in row:
            # write the current row to the output file
            writer.writerow(row)
