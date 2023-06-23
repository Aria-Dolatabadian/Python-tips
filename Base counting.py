import csv

def count_bases(sequence):
    base_count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for base in sequence:
        if base in base_count:
            base_count[base] += 1
    return base_count

sequence = 'ACGACGACATAGACGATAAGCGCAGATATATTACGAACGACAGCACGC'
result = count_bases(sequence)

# Write results to CSV file
filename = 'base_counts.csv'
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Base', 'Count'])
    for base, count in result.items():
        writer.writerow([base, count])

print("Results written to", filename)
