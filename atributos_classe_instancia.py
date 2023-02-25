class Estudante:
    escola = "DIO"

    def __init__(self, nomne, matricula):
        self.nome = nomne
        self.matricula = matricula

    
    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


aluno_1 = Estudante("Henrique", 1)
aluno_2 = Estudante("Luciana", 2)

mostrar_valores(aluno_1, aluno_2)

aluno_2.matricula = 3
mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "Eita"
aluno_3 = Estudante("Ytalo", 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)


