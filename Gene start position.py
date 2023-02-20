DNA = "AAAATCAAAAATCAA"
i=[]
while True:
    if 'ATC' in DNA:
        i.append(DNA.find('ATC'))
        DNA=DNA.replace('ATC','atc',1)
    else:
        break
print(i)
