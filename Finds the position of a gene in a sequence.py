# Sample chromosome sequence
chromosome_sequence = "ATCGACGAGGGCGACGACTAGGCAGCAGCATCGATAGACGACTCGATCG"

# Define a gene sequence to search for
gene_sequence = "GACGACTA"

# Find the gene's location(s) on the chromosome
gene_locations = []
start = 0

while True:
    index = chromosome_sequence.find(gene_sequence, start)
    if index == -1:
        break
    gene_locations.append(index +1)
    start = index + 1

# Print the gene locations
if gene_locations:
    print("Gene found at positions:", gene_locations)
else:
    print("Gene not found on the chromosome.")
