from abc import ABC


class ControleRemoto(ABC):
    
    def ligar(self):
        pass

    def desligar(self):
        pass

class Controletv(ControleRemoto):
    pass


controle = Controletv()

controle.ligar()
controle.desligar()
