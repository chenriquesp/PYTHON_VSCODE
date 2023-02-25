from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTv(ControleRemoto):
    def ligar(self):
        print("Ligando Tv...")
    
    def desligar(self):
        print("desligando Tv...")

    @property
    def marca(self):
        return "LG"


controle = ControleTv()

controle.ligar()
controle.desligar()
print(controle.marca)
