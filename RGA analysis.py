genes = ['RLK',
'RLK','TNL','TNL','RLK','RLK','RN','RLK','RLK','RLK','RLK','RLK','RLK','RLK','RLK','RLK','RLK','RLP',
'RLK','RLK','RLK','RLP','TX','NL','NBS','TX','RLK','RLK','RLK','RLK','TX','TX','TX','RLK','RLK','CN',
'RLK','RLP','RLK','RLK','CNL','NL','RLP','RLK','CN','RLK','RLK','RLK','TX','RLK','RLK','RLK','RLK',
'RLK','RLK','RLP','RLK','RLK','RLK','RLK','NBS','RLK','RLK','NL','RLK','RLK','RLK','RLK','RLK',
'NBS',
'NBS',
'RLK',
'OTHER',
'RLK',
'RLK',
'RLK',
'RLK',
'RLK',
'RLK',
'RLP',
'RLK',
'RLK',
'RNL'
]

print ("RGAs list : " + str(genes))

counter = 0
for i in genes:
    counter = counter + 1
print ("Total number of RGAs: " + str(counter))

import collections
print (('Duplicated genes:'),([item for item, count in collections.Counter(genes).items() if count > 1]))

count = genes.count('RLK')
print('RLK:', count)
count = genes.count('TNL')
print('TNL:', count)
count = genes.count('RN')
print('RN:', count)
count = genes.count('RLP')
print('RLP:', count)
count = genes.count('TX')
print('TX:', count)
count = genes.count('NL')
print('NL:', count)
count = genes.count('NBS')
print('NBS:', count)
count = genes.count('CN')
print('CN:', count)
count = genes.count('CNL')
print('CNL:', count)
count = genes.count('TN')
print('TN:', count)
count = genes.count('OTHER')
print('OTHER:', count)
count = genes.count('RNL')
print('RNL:', count)
