Seq = "AAAAAAAAAAUAGAAAAA"
Codon = ['UGA', 'UAG', 'UAA']
def checkIfAny(Seq, Codon):
  for codes in Codon:
    if codes in Seq:
      return (True, codes)
  return (False, "")
result = checkIfAny(Seq, Codon)
if result[0]:
   print('Stop codon found in the seq: ', result[1])
