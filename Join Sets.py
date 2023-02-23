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

#Keep ONLY the Duplicates

#The intersection_update() method will keep only the items that are present in both sets.

RGA1 = {"RLK", "RLP", "CNL", "TNL"}
RGA2 = {"RLK", "RLP", "TX", "NL"}
RGA1.intersection_update(RGA2)
print(RGA1)

#The intersection() method will return a new set, that only contains the items that are present in both sets.

RGA1 = {"RLK", "RLP", "CNL", "TNL"}
RGA2 = {"RLK", "RLP", "TX", "NL"}
RGA3 = RGA1.intersection(RGA2)
print(RGA3)
