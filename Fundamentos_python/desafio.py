
""" T = str(input())
tamanho_T = 0

for x in T:
  tamanho_T += 1

if tamanho_T <= 140:
  print("TWEET")
else:
  print("MUTE") """

""" month = int(input())

months_dict = {
  1 : "January", 2 : "February", 3 : "March", 4 : "April", 5 : "May", 6 : "June", 7 : "July", 8: "August",
  9 : "September", 10 : "October", 11 : "November", 12 : "December"
}

print(f"{months_dict[month]}") """

''' Entrada de repetições do teste '''
n = int(input("Digite a quantidade de testes: "))

while(n > 0):
   
    # Coleta dos números para serem comarados
    numero = str(input("Digite dois números: "))

    #Local de armazenamento dos números
    numero_a = ""
    numero_b = ""
    indece = 0

    #Seperando os numeros para tratar
    #amazenando numenro A
    for letra in numero:
        if not letra.isspace(): #para ao encontra um espaço
            numero_a += letra
        else:
            #armazena o indece da string após encontrar o espaço
            indece = numero.find(letra) + 1
            break # sai do for
    
    #Amazenaando numero B
    for letra in range(indece,numero.__len__()):
        numero_b += numero[letra]
    
    # Tratando e imprimento o resultado
    if numero_a.__contains__(numero_b) :
        print("encaixa")
    else:
        print("não encaixa")
    
    #decremento do teste
    n -= 1
