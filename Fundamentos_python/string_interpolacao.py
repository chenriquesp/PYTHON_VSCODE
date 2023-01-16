nome = "Guilherme"
idade = 28

dados = {"nome":"Guilherme", "idade":28}

Saldo = 45.58964

print("Nome: %s Idade: %d" %(nome, idade))

print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {1} Idade: {0}".format(idade, nome))

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {Saldo}")
print(f"Nome: {nome} Idade: {idade} Saldo: {Saldo:.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {Saldo:8.2f}")
