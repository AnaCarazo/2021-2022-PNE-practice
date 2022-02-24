from Seq1 import Seq
# -- Create a Null sequence
s1 = Seq()
# -- Create a valid sequence
s2 = Seq("ACTGA")
# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

list_s = [s1, s2, s3]

for i in range(0, len(list_s)):
    print("Sequence " + str(i + 1) + ": (Length:", str(list_s[i].len()) + ")", list_s[i])