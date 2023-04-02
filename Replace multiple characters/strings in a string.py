Seq = "ATACAGATGACAGATAGATGA"
def replace(Seq, Rep, Seq2):
  for elem in Rep:
    if elem in Seq:
      Seq = Seq.replace(elem, Seq2)
  return Seq
Seq2 = replace(Seq, ['A', 'C'] , "G")
print(Seq2)
