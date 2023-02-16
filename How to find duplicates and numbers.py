genes = ['RLP','TNL','TNL','CNL','CNL','RLK','RLP','RLP']

import collections
print (('Duplicates genes:'),([item for item, count in collections.Counter(genes).items() if count > 1]))

count = genes.count('NBS')
print('NBS:', count)
count = genes.count('TNL')
print('TNL:', count)
count = genes.count('CNL')
print('CNL:', count)
count = genes.count('RLK')
print('RLK:', count)
count = genes.count('RLP')
print('RLP:', count)
