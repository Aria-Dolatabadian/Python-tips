#List Comprehension
RGA = ["CNL", "TNL", "RLK", "RLP"]
NBS = []
for x in RGA:
  if "NL" in x:
    NBS.append(x)
print(NBS)
print('....................')
#OR
NBS = [x for x in RGA if "NL" in x]
print(NBS)
