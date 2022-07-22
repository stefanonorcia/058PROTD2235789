from model.distributore import Distributore
from model.rubrica import Rubrica

print("Hello rubrica!")

rubrica = Rubrica()
rubrica.aggiungiContatto("stefano", "norcia", "45678909")

distributore = Distributore()
distributore.aggiungiBibita("A", "acqua", 1.0)
distributore.aggiungiBibita("B", "birra", 2.0)
distributore.aggiungiBibita("C", "coca", 1.5)

distributore.aggiungiTessera(1, 10.0)
distributore.aggiungiTessera(2, 20.0)

distributore.aggiungiColonna(1, "acqua", 1)
distributore.aggiungiColonna(2, "birra", 3)
distributore.aggiungiColonna(3, "coca", 3)
distributore.aggiungiColonna(4, "acqua", 4)

distributore.eroga("A", 2)



