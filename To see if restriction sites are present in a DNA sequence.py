import re
dna = "AAAGGACCAAAAAAAAAAA"
if re.search(r"GGACC", dna) or re.search(r"GGTCC", dna):
    print("restriction site found!")
else:
    print("restriction site not found!")
