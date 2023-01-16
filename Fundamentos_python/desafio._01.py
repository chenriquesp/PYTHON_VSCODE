''' 
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída. 
'''
n = int(input())

while(n > 0):

    ''' 
    TODO  Verifique, para cada entrada A e B, se os dois valores são compatíveis e imprima se
    "encaixa" ou "não encaixa" para cada uma das relações N vezes.
    '''
    numero = input().split()

    numero_a = numero[0]
    numero_b = numero[1]
    

    if len(numero_b) > len(numero_a):
        print("nao encaixa")
    else:
        print("passou")
        if numero_a.endswith(numero_b):
            print("encaixa")
        else:
            print("nao encaixa")
    
    n -= 1
