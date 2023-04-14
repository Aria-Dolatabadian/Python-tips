import re
dna = "CTGCATTATATCGTACGAAATTATACGCGCGAAA"
matches = re.finditer(r"[AT]{6,}", dna)
result = []
for m in matches:
    result.append(m.group())
print(result)
