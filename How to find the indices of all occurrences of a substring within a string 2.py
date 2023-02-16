import re
print([m.start() for m in re.finditer('UTC', 'UTCATCGATACAUTCTGACATGACATATAUTCTAGACATGAUTC')])
