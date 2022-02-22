import Seq0
seq = Seq0.seq_read_fasta("U5")
rev = Seq0.seq_reverse(seq)
print("Frag:", rev[0], "\nRev:", rev[1])
