NBS = {"CNL", "TNL"}
TM = {"RLK", "RLP"}
NBS.update(TM)
print(NBS)



#This returns an error because it is impossible to add a set to a list but it is possible to add a list to a set.
NBS = ["CNL", "TNL"]
TM = {"RLK", "RLP"}
NBS.update(TM)
print(NBS)
