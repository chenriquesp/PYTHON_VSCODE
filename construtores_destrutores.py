
class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a instânca...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Destruindo a instância da classe.")
    def falar(self):
        print("auau")

c = Cachorro("Xola", "Caramelo")
c.falar()
