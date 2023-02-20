list1 = ["CNL", "TNL"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
#OR
for x in list2:
  list1.append(x)
print(list1)
#OR
list1 = ["RLK", "RLP"]
list2 = [10, 20]
list1.extend(list2)
print(list1)
