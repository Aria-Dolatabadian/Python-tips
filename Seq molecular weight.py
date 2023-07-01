from Bio.SeqUtils import molecular_weight
from Bio.Seq import Seq

# Create a DNA sequence
dna_seq = Seq("ATCGATCGATCG")

# Calculate the molecular weight
mw = molecular_weight(dna_seq)

print("Molecular Weight:", mw)
