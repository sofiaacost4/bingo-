import random
#Aluna: Sofia Costa
#Turma: Infoweb 1 ano
#Professor: Alexandre

#constantes (não devem mudar ao decorrer do jogo)

num_linhasr = 2
num_linhasd = 3
num_colunasr = 3
num_colunasd = 4
num_cartelasr = 2
num_cartelasd = 4
modo_rapido = 0
modo_demorado = 1

def imprimir_cartelar(cartela):
    print(cartela[0][0], cartela[0][1], cartela[0][2])
    print(cartela[1][0], cartela[1][1], cartela[1][2])

def imprimir_cartelad(cartela):
    print(cartela[0][0], cartela[0][1], cartela[0][2], cartela[0][3])
    print(cartela[1][0], cartela[1][1], cartela[1][2], cartela[1][3])
    print(cartela[2][0], cartela[2][1], cartela[2][2], cartela[2][3])

def criar_cartela1(linhas, colunas):
    cartela_matriz1 = [[0 for _ in range(colunas)] for _ in range(linhas)]
    x = 0
    y = 0
    while y <= 1:
        if x == 0:
         cartela_matriz1[y][x] = random.randint(1,10)
        if x == 1:
         cartela_matriz1[y][x] = random.randint(11,20)
        if x == 2:
         cartela_matriz1[y][x] = random.randint(21,30)
         y = y + 1
         x = -1
        x = x + 1
    return cartela_matriz1
def criar_cartela2(linhas, colunas):
    cartela_matriz2 = [[0 for _ in range(colunas)] for _ in range(linhas)]
    x = 0
    y = 0
    while y <= 1:
        if x == 0:
         cartela_matriz2[y][x] = random.randint(1,10)
        if x == 1:
         cartela_matriz2[y][x] = random.randint(11,20)
        if x == 2:
         cartela_matriz2[y][x] = random.randint(21,30)
         y = y + 1
         x = -1
        x = x + 1
    return cartela_matriz2

def escolher_modo():
    print('Indique o modo de jogo: \n0 - RÁPIDO \n1 - DEMORADO\n')
    modo = int(input())
    if modo != 0 or modo != 1:
       print("Modo inválido.")
       print('Indique o modo de jogo: \n0 - RÁPIDO \n1 - DEMORADO\n')
       modo = int(input())

cartelar_matriz1 = criar_cartela1(num_linhasr, num_colunasr)
cartelar_matriz2 = criar_cartela2(num_linhasr, num_colunasr)

escolher_modo()
print("Jogador 1")
criar_cartela1(num_linhasr, num_colunasr)
imprimir_cartelar(cartelar_matriz1)
print("Jogador 2")
criar_cartela2(num_linhasr, num_colunasr)
imprimir_cartelar(cartelar_matriz2)
