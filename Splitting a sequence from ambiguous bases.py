import re
dna = "CAXGCATACTACTXACGACATAATXCG"
runs = re.split(r"[^ATGC]", dna)
print(runs)
