#The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.

RGA1 = {"RLK", "RLP", "CNL", "TNL"}
RGA2 = {"RLK", "RLP", "TX", "NL"}
RGA3 = RGA1.symmetric_difference(RGA2)
print(RGA3)
