# Remove Specified Item
RGA = ["RLK", "RLP", "NBS"]
RGA.remove("NBS")
print(RGA)
# Remove Specified Index
# Remove the second item:
Gene = ["CNL", "TNL", "TX"]
Gene.pop(1)
print(Gene)
# Remove the last item:
RGAs = ["TN", "NL", "CN"]
RGAs.pop()
print(RGAs)
# Remove the first item:
Genes = ["RLK", "RLP", "CNL"]
del Genes[0]
print(Genes)
# Delete the entire list:
gene = ["TNL", "CNL", "TX"]
del gene
# Clear the List
rga = ["RLK", "TX", "RLP"]
rga.clear()
print(rga)
