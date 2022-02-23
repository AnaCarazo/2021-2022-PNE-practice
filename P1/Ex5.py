from Seq1 import Seq
# -- Create a Null sequence
s1 = Seq()

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

list_s = [s1, s2, s3]
for s in list_s:
    dict_list = s.seq_count()
    print("Sequence 1: (Lenght:", s1.len(),")", s1, "\n", dict_list.items())



