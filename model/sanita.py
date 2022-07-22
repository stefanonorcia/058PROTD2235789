class Sanita:
    def __init__(self):
        self.dottori = {}
        self.pazienti = {}

    def aggiungiDottore(self, nome, cognome, codiceFiscale, matricola):
        pass

    def aggiungiPaziente(self, nome, cognome, codiceFiscale, codicePaziente):
        pass

    # restituisce il paziente dato il codice
    def getPaziente(self, codicePaziente):
        pass

    # restituisce il medico data la matricola
    def getDottore(self, matricola):
        pass

    # assegna un aziente a un medico
    def assegnaMedico(self, matricola, codice):
        pass

    # restituisce una stringa contenente l'elenco dei pazienti assegnati a un medico
    def getPazienti(self, matricola):
        pass

    # salva sul file pazienti.txt l'elenco dei pazienti
    def salvaPazienti(self):
        pass

# sia il dottore che il paziente hanno come attributo nome cognome e codice fiscale
# il paziente ha un codice univoco e il dottore una matricola


class Dottore:
    def __init__(self, nome, cognome, coficeFiscale, matricola):
        self.matricola = matricola
        self.pazienti = []


class Paziente:
    def __init__(self, nome, cognome, coficeFiscale, codice):
        self.codice = codice
        self.dottori = []
