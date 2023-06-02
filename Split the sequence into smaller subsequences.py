#Split the sequence into smaller subsequences
from bioinfokit import analys
#Split the sequences with overlap
# analys.Fasta.split_seq(seq='ATGACAGATATATAGACAGATAGCAT', seq_size=3, outfmt='fasta')
#Split the sequences without overlap
analys.Fasta.split_seq(seq='ATACAGATATATACAGATAGAAGCAT', seq_size=3, seq_overlap=False, outfmt='fasta')
