#TypeError: seq_read_fasta() takes 1 positional argument but 2 were given
from Seq1 import Seq
# -- Create a Null sequence
s = Seq()

# -- Initialize the null seq with the given file in fasta format
s.seq_read_fasta("U5")
dict_list = s.count()
print("Sequence U5: (Lenght:", s.len(),")", s, "\nBases:", dict_list, "\nRev:", s.seq_reverse(), "\nComp:", s.complementary_seq())