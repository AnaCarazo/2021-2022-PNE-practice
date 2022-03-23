class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):  # we do not need to return anything in this function
        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
        if not self.valid_sequence():
            self.strbases = "ERROR"
            print("ERROR!!")
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

    def __str__(self):
        """Method called when the object is being printed"""
        return self.strbases

    def len(self):
        return len(self.strbases)

    @staticmethod
    def print_seqs(seq_list):
        i = 0
        for seq in seq_list:
            print(f"Sequenece {i}: (Lenght: {seq.len()}) {seq}")
            i += 1

#main program
list_seq = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
result = Seq.print_seqs(list_seq)