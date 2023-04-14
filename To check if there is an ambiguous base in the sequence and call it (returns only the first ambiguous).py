import re
dna = "CGATNCGGAACGATC"
if re.search(r"[^ATGC]", dna):
    print("ambiguous base found!")
else:
    print("ambiguous base not found!")
m = re.search(r"[^ATGC]", dna)
if m:
    ambig = m.group()
    print("the base is " + ambig)
