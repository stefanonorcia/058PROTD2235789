class Rubrica:
    def __init__(self):
        self.contatti = []

    def aggiungiContatto(self, nome, cognome, telefono):
        pass

    def rimuoviContatto(self, position):
        pass

    # ricerca la key in nome cognome telefono di ogno contatto
    def cercaContatto(self, key):
        pass
    # restituisce una stringa contenente nome cognome e telefono
    def stampaContatto(self, position):
        pass
    # restituisce una stringa con elenco dei contatti, uno per riga
    def listaContatti(self):
        pass


class Contatto:
    def __init__(self, nome, cognome, telefono):
        self.nome = nome;
        self.cognome = cognome
        self.telefono = telefono

    def __str__(self):
        return self.nome + ' ' + self.cognome + ' ' + self.telefono
