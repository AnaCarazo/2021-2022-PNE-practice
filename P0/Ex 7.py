import Seq0
seq = Seq0.seq_read_fasta("U5")
frag = seq[:20]
print("Frag:", frag)
complementary = Seq0.complementary_seq(frag)
print("Comp:", complementary)