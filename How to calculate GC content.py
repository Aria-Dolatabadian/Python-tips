DNA="ATCG"
c=DNA.count("C")
g=DNA.count("G")
print('GC content(%):',(c + g) / len(DNA) * 100)
