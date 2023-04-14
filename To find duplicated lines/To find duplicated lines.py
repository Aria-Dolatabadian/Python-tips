from collections import Counter
with open('Seq.csv') as f:
    c = Counter(c.strip().upper() for c in f if c.strip())
    for line in c:
        if c[line] > 1:
            print(line)
            
            
