class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Mamifefo(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)
        


class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)


class Gato(Mamifefo):
    pass


class Onitorinco(Mamifefo, Ave):
    def __init__(self, cor_pelo, **kw):
        print(Onitorinco.__mro__)
        print(Onitorinco.mro())
        super().__init__(cor_pelo, **kw)


gato = Gato(nro_patas=4, cor_pelo="preto")
print(gato)

onitorinco = Onitorinco(nro_patas=2, cor_pelo="branco", cor_bico="Laranja")
print(onitorinco)
