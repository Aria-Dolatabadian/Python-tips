Seq = "AAUGAAAAAAUAAAAAAAAUAGAAA"
Codon = ['UGA', 'UAA', 'UAG']
result = all(([True if subStr in Seq else False for subStr in Codon]))
if result:
   print('All codons from list found in the Seq')
else:
  print('Not all the codons from list found in the Seq')
