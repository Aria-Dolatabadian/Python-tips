import re
dna = "ATCGCGYAATTCAC"
if re.search(r"[^ATGC]", dna):
    print("ambiguous base found!")
else:
    print("ambiguous base not found!")
