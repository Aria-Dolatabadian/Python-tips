import csv
import random

# Define the number of rows and columns for the CSV file
num_genes = 10000
num_cols = 4

# Define the range for the start and end positions
start_range = 1000000
end_range = 5000000

# Define the gene and chromosome labels
genes = [f"Bn{i}" for i in range(1, num_genes+1)]
chromosomes = [f"A{i:02}" for i in range(1, 11)]

# Generate the data for each row
data = []
for gene in genes:
    chrom = random.choice(chromosomes)
    start = random.randint(start_range, end_range)
    end = random.randint(start, end_range)
    data.append([gene, chrom, start, end])

# Write the data to a CSV file
with open('gene_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Gene', 'Chromosome', 'Start', 'End'])
    writer.writerows(data)
