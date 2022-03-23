class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases

        print("New sequence created!")

    def __str__(self): # si no  ponemos esto se imprime cómo está guardado en la memoria, pero no como un string
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)


# --- Main program
s1 = Seq("AGTACACTGGT")
s2 = Seq("CGTAAC")

# -- Printing the objects
print(f"Sequence 1: {s1}") #cuando queremos imprimir un objero, la __str__ function is called automatically
print(f"  Length: {s1.len()}")
#print("  Length:", s1.len()) esta es la forma que hemos usado siempre
print(f"Sequence 2: {s2}")
print(f"  Length: {s2.len()}")