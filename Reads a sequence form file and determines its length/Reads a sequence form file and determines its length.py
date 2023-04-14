DNA = open("FASTA.txt")
my_DNA = DNA.read()
dna_length = len(my_DNA)
print("sequence is " + my_DNA +  " and length is " + str(dna_length))
