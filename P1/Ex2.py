from Seq1 import Seq
print("-----| Exercise 2 |------")
# -- Creating a Null sequence
s1 = Seq()
# -- Creating a valid sequence
s2 = Seq("TATAC")

list_s = [s1, s2]

for i in range(0, len(list_s)):
    print("Sequence " + str(i + 1) + ":", list_s[i])