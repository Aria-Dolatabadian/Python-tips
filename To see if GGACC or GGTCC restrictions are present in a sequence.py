import re
dna = "ATCGGTCCGAATTCAC"
if re.search(r"GG(A|T)CC", dna):
    print("restriction site found!")
else:
    print("restriction site not found!")
