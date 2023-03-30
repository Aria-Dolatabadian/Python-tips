Seq1="AATACGATGACGACGACGACTACT"
Seq2="ATACGATGACGACGACGACTACT"

if Seq1 is Seq2:
    print('Both Seqs are equal')
else:
    print('Seqs are not equal')
    print("ID of Seq1:" , id(Seq1))
    print("ID of Seq2:", id(Seq2))
