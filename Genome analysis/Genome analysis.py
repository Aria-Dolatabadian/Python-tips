import csv
import collections
napus = open('D:\python\Bnapus.csv', 'r')
genome = csv.DictReader(napus)
gene = collections.defaultdict(int)

for input in genome:
    gene[input['Chrom']] += 1 if input['Class'] in ['RLK'] else 0
print(gene)
for x in gene:
  print((x),(':'), (gene[x]))
