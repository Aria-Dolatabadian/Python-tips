import re
dna = "AAAGCAGCAAAAAGCGGCAAAAAAA"
if re.search(r"GC[ATGC]GC", dna):
    print("restriction site found!")
else:
    print("restriction site not found!")
