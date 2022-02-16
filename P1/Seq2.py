class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases): #we do not need to return anything in this function

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
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