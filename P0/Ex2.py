import Seq0
filename = Seq0.valid_filename()
sequence = Seq0.seq_read_fasta(filename) #you need to generate the path
print("The first 20 nucleotides are: ", sequence[:20])