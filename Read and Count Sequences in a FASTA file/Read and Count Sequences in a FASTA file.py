from Bio import SeqIO
handle=open('sequence.fasta','rt')
seqobj=SeqIO.parse(handle,'fasta')
sequences=[seq for seq in seqobj]
print(sequences)
#number of sequences
print(len(sequences))
print(sequences[0].name)
print(sequences[1].name)
print(sequences[9].name)
