class Conto:
    def __init__(self, nome, conto):
            self.nome = nome
            self.conto = conto

class ContoCorrente(Conto):
    def __init__(self, nome, conto, importo):
        super().__init__(nome, conto)
        self.__saldo = importo

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, importo):
        self.preleva(self.__saldo)
        self.deposita(importo)

    def preleva(self, importo):
        self.__saldo -= importo     
    
    def deposita(self, importo):
        self.__saldo += importo
    
    def descrizione(self):
        print(self.nome, self.conto, self.__saldo)

class GestioneContiCorrenti:

    @staticmethod
    def bonifico(sorgente, destinazione, importo):
        sorgente.preleva(importo)
        destinazione.deposita(importo)

c1 = ContoCorrente("raf", "10", 100)
c2 = ContoCorrente("naty", "22", 50)
c1.descrizione()
GestioneContiCorrenti.bonifico(c1, c2, 50)
c2.descrizione()