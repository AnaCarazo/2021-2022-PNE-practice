from Seq1 import Seq
# -- Create a Null sequence
s1 = Seq()

# -- Create a valid sequence
s2 = Seq("ACTGA")

# -- Create an invalid sequence
s3 = Seq("Invalid sequence")

print("Sequence 1: (Lenght:", s1.len(),")", s1, "\nSequence 2: (Lenght:", s2.len(),")", s2, "\nSequence 3: (Lenght:", s3.len(),")", s3)