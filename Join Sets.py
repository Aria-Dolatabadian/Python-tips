TM = {"RLK", "RLP"}
NBS ={"CNL","TNL"}
RGAs = TM.union(NBS)
print(RGAs)
#Or
RGAs = NBS.union(TM)
print(RGAs)

#The update() method inserts the items in set2 into set1:

TM = {"RLK", "RLP"}
NBS ={"CNL","TNL"}
TM.update(NBS)
print(TM)
#Or
NBS.update(TM)
print(NBS)
