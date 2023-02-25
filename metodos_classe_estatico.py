class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade>= 18


p1 = Pessoa("Carlos", 48)
p2 = Pessoa.criar_de_data_nascimento(1974, 10, 27, "Henrique")
        
print(p1.nome, p1.idade)
print(p2.nome, p2.idade)

print(Pessoa.e_maior_idade(p1.idade))