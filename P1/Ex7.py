#no entiendo xq el for loop lo hace solo una vez y no itinera por toda la lista
from Seq1 import Seq
# -- Create a Null sequence
s1 = Seq()
# -- Create a valid sequence
s2 = Seq("ACTGA")
# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

list_s = [s1, s2, s3]
list_num= []

for i in range(1, len(list_s) + 1):
    list_num.append(i)
zipped = zip(list_s, list_num)
for s, n in zipped:
    dict_list = s.count()
    print("Sequence", n, ": (Lenght:", s.len(),")", s, "\nBases:", dict_list, "\nRev:", s.seq_reverse())