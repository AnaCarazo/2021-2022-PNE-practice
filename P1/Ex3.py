from Seq1 import Seq
# -- Create a Null sequence
s1 = Seq()
# -- Create a valid sequence
s2 = Seq("ACTGA")
# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

list_seq = [s1, s2, s3]
list_num = []
for i in range(1, len(list_seq) + 1):
    list_num.append(i)
zipped = zip(list_num, list_seq)
for s, n in zipped:
    print("Sequence", n, ":", s)
