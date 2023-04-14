import re
dna = "CGCTCNTAGATGCGCRATGACTGCAYTGC"

matches = re.finditer(r"[^ATGC]", dna)
for m in matches:
    base = m.group()
    pos  = m.start()
    print(base + " found at position " + str(pos))
