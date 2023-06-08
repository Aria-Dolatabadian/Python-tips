from Bio import SeqIO
handle=open('sequence.fasta','rt')
seqobj=SeqIO.parse(handle,'fasta')
sequences=[seq for seq in seqobj]
print(sequences)
#or
with open("sequence.fasta") as handle:
    for record in SeqIO.parse(handle, "fasta"):
        print(record.id)

records = list(SeqIO.parse("sequence.fasta", "fasta"))
print(records[0].id)  # first record
print(records[-1].id)  # last record
