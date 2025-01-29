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

def imprimir_cartelar(cartela):
    print(cartela[0][0], cartela[0][1], cartela[0][2])
    print(cartela[1][0], cartela[1][1], cartela[1][2])

def imprimir_cartelad(cartela):
    print(cartela[0][0], cartela[0][1], cartela[0][2], cartela[0][3])
    print(cartela[1][0], cartela[1][1], cartela[1][2], cartela[1][3])
    print(cartela[2][0], cartela[2][1], cartela[2][2], cartela[2][3])

def criar_cartela(linhas, colunas):
    cartela_matriz = [[0 for _ in range(colunas)] for _ in range(linhas)]
    x = 0
    y = 0
    while y <= 1:
        if x == 0:
         cartela_matriz[y][x] = random.randint(1,10)
        if x == 1:
         cartela_matriz[y][x] = random.randint(11,20)
        if x == 2:
         cartela_matriz[y][x] = random.randint(21,30)
         y = y + 1
         x = -1
        x = x + 1
    return cartela_matriz


cartelar_matriz = criar_cartela(num_linhasr, num_colunasr)
imprimir_cartelar(cartelar_matriz)
