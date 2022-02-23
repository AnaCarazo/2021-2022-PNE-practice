#no entiendo xq el for loop lo hace solo una vez y no itinera por toda la lista
from Seq1 import Seq
# -- Create a Null sequence
s1 = Seq()

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

list_s = [s1, s2, s3]
for s in list_s:
    dict_list = s.count()
    print("Sequence 1: (Lenght:", s.len(),")", s, "\nBases:", dict_list, "\nRev:", s.seq_reverse(), "\nComp:", s.complementary_seq())

#cambiar para que se escriba "Sequence: n", siemdo n el número que corresponda empezando en 1