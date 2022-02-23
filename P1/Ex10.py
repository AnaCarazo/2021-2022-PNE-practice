#TypeError: seq_read_fasta() takes 1 positional argument but 2 were given
from Seq1 import Seq
list_seq = ["U5", "ADA", "FRAT1", "FXN"]
for l in list_seq:
    s = Seq()
    seq = s.seq_read_fasta(l)
    base = s.most_frecuent_base(seq)
    print("Gene", l + ":", "Most frequent Base:", base)