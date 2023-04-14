import re
dna = "AAAATGCAAAAAA"
if re.search(r"TGC", dna):
    print("restriction site found!")
else:
    print("restriction site not found!")
