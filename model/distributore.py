class Distributore:
    def __init__(self):
        self.bibite = {}
        self.tessere = {}
        self.colonne = {}

    def aggiungiBibita(self, codice, nome, prezzo):
        pass

    def aggiungiTessera(self, codice, credito):
        pass

    def aggiungiColonna(self, numero, bibita, quantita):
        pass

    def getPrezzo(self, codiceBevanda):
        pass

    def getNome(self, codiceBevanda):
        pass

    def getCredito(self, codiceTessera):
        pass

    def eroga(self, codiceBibita, codiceTessera):
        pass




class Bibita:
    def __init__(self, codice, nome, prezzo):
        self.codice = codice
        self.nome = nome
        self.prezzo = prezzo


class Tessera:
    def __init__(self, codice, credito):
        self.codice = codice
        self.credito = credito


class Colonna:
    def __init__(self, numero, bibita, quantita):
        self.numero = numero
        self.bibita = bibita
        self.quantita = quantita
