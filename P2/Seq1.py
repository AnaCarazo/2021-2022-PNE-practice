class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases="NULL"):

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
        if self.strbases == "NULL":
            print("NULL Seq created")

        elif not self.valid_sequence():
            self.strbases = "ERROR"
            print("INVALID Seq!")

        else:
            print("New sequence created!")

    def valid_sequence(self):
        valid = True
        i = 0
        while i < len(self.strbases) and valid:
            c = self.strbases[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid

    def __str__(self): # si no  ponemos esto se imprime cómo está guardado en la memoria, pero no como un string
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

#----Ex4-----
    def len(self):
        """Calculate the length of the sequence"""
        if self.strbases == "NULL" or not self.valid_sequence():
            return 0
        else:
            return len(self.strbases)

# ----Ex5-----
    def count_base(self):
        if self.strbases == "NULL" or not self.valid_sequence():
            list_count = [0, 0, 0, 0]
        else:
            list_count = [self.strbases.count("A"), self.strbases.count("C"), self.strbases.count("T"), self.strbases.count("G")]
        return list_count

# ----Ex6-----
    def count(self):
        if self.strbases == "NULL" or not self.valid_sequence():
            list_count = [0, 0, 0, 0]
            list_basis = ["A", "C", "T", "G"]
            dict_list = dict(zip(list_basis, list_count))
        else:
            list_count = [self.strbases.count("A"), self.strbases.count("C"), self.strbases.count("T"), self.strbases.count("G")]
            list_basis = ["A", "C", "T", "G"]
            dict_list = dict(zip(list_basis, list_count))
        return dict_list

# ----Ex7-----
    def seq_reverse(self):
        if self.strbases == "NULL":
            return "NULL"
        elif not self.valid_sequence():
            return "ERROR"
        else:
            reverse = self.strbases[::-1]
            return reverse

# ----Ex8-----
    def complementary_seq(self):
        if self.strbases == "NULL":
            return "NULL"
        elif not self.valid_sequence():
            return "ERROR"
        else:
            complementary = ""
            for c in self.strbases:
                if c == "A":
                    complementary += "T"
                elif c == "T":
                    complementary += "A"
                elif c == "C":
                    complementary += "G"
                else:
                    complementary += "C"
            return complementary

# ----Ex9-----
    def seq_read_fasta(self, filename):
        f = open("./seq_dna/" + filename + ".txt", "r").read()
        seq = f[f.find("\n") + 1:].replace("\n", "")
        self.strbases = seq
        #cuando estás cambiando un attribute de la lista, en este caso self.strbases, no hace falta to return anything

# ----Ex10-----
    def most_frecuent_base(self):
        list_count = [self.strbases.count("A"), self.strbases.count("C"), self.strbases.count("T"), self.strbases.count("G")]
        list_basis = ["A", "C", "T", "G"]
        max_base = max(list_count)
        index_base = list_count.index(max_base)
        return list_basis[index_base]
        #dict_list = dict(zip(list_basis, list_count))
        #import operator
        #dict_list_sorted_by_apparences = sorted(dict_list.items(), key=operator.itemgetter(1), reverse=True)
        #return dict_list_sorted_by_apparences[0][0]

# ----Ex6, practice 2-----
    def frag_10bases(self, n1, n2):
        return self.strbases[int(n1) * 10: int(n2) * 10]


