class Rubrica:
    def __init__(self):
        self.contatti = []

    def aggiungiContatto(self, nome, cognome, telefono):
        pass

    def rimuoviContatto(self, position):
        pass

    def cercaContatto(self, key):
        pass

    def stampaContatto(self, position):
        pass

    def listaContatti(self):
        pass


class Contatto:
    def __init__(self, nome, cognome, telefono):
        self.nome = nome;
        self.cognome = cognome
        self.telefono = telefono
