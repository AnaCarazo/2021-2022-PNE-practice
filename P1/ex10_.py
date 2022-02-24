from Seq1 import Seq
# -- Create a Null sequence
s = Seq()
# -- Initialize the null seq with the given file in fasta format
s.seq_read_fasta("U5")
print("Gene U5: Most frequent Base:", s.most_frecuent_base())