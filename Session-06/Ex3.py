class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases): #we do not need to return anything in this function
        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
        if not self.valid_sequence():
            self.strbases = "ERROR"
            print("ERROR!!")
        else:
            print("New sequence created!")

    #esta función se puede usar antes of instanciating a class, así nos podemos asegurar de que lo que instanciamos es una valid sequence
    @staticmethod #this function spects a normal argument, not self, por tanto dentro de la función tmb cambiamos eso
    def valid_sequence2(sequence):
        valid = True
        i = 0
        while i < len(sequence) and valid:
            c = sequence[i]
            if c != "A" and c != "C" and c != "G" and c != "T":
                valid = False
            i += 1
        return valid

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

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)

class Gene(Seq):
    """This class is derived from the Seq Class
       All the objects of class Gene will inheritate
       the methods from the Seq class
    """
    def __init__(self, strbases, name=""):

        # -- Call first the Seq initilizer and then the
        # -- Gene init method
        super().__init__(strbases)
        self.name = name
        print("New gene created")

    def __str__(self):
        """Print the Gene name along with the sequence"""
        return self.name + "-" + self.strbases

    def generate_seqs(pattern, number):
        list_seqs = []
        for i in range(0, number):
            seq = pattern
            list_seqs.append(seq)
            pattern = pattern + list_seqs[0]
        return list_seqs


#main program
seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs("Sequence", n, ":", s, ", Lenght:", s.len())

print()
print("List 2:")
print_seqs(seq_list2)