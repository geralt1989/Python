class Persona:
    def __init__(self, nome, cognome, anno_di_nascita, residenza):
        self.nome = nome
        self.cognome = cognome
        self.anno_di_nascita = anno_di_nascita
        self.residenza = residenza
    
    def profilo_personale(self):
        return f"nome: {self.nome}, cognome: {self.cognome}, anno di nascita: {self.anno_di_nascita}, residenza: {self.residenza}"

    def __str__(self):
        return f"nome: {self.nome}, cognome: {self.cognome}"


class Sviluppatore(Persona):
    def __init__(self, nome, cognome, anno_di_nascita, residenza, posizione, paga_annua):
        super().__init__(nome, cognome, anno_di_nascita, residenza)
        self.posizione = posizione
        self.paga_annua = paga_annua

    def profilo_impiegato(self):
        return super().profilo_personale() + f", posizione: {self.posizione}, paga annua: {self.paga_annua}"

    def __str__(self):
        return f"posizione: {self.posizione}, nome: {self.nome}, cognome: {self.cognome}"

s1 = Persona("luca", "rossi", 1989, "roma")
s2 = Sviluppatore("raffaele", "ficcad", 1976, "roma", "capo", 60000)
print(s1.profilo_personale())
print("#########")
print(s2.profilo_impiegato())