# Loop Through a List
RGA = ["RLK", "RLP", "NBS"]
for x in RGA:
  print(x)
print('..................')
# Loop Through the Index Numbers
RGAs = ["CNL", "TNL", "NL"]
for i in range(len(RGAs)):
  print(RGAs[i])
print('..................')
# Using a While Loop
Gene = ["CNL", "TNL", "NBS"]
i = 0
while i < len(Gene):
  print(Gene[i])
  i = i + 1
print('..................')
# Looping Using List Comprehensive
Genes = ["NBS", "CNL", "RLK"]
[print(x) for x in Genes]
