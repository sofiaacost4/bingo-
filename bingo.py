import random
#Aluna: Sofia Costa
#Turma: Infoweb 1 ano
#Professor: Alexandre

#constantes (não devem mudar ao decorrer do jogo)

num_linhasr = 2
num_linhasd = 3
num_colunasr = 3
num_colunasd = 4

def checar_cartela1():
 x = 0
 y = 0
 if modo == 0:
  while y <= 2:

        if x == 0 and cartela_matriz1[y][x] == d:
         cartela_matriz1[y][x] = f"({cartela_matriz1[y][x]})"
        if x == 1 and cartela_matriz1[y][x] == d:
         cartela_matriz1[y][x] = f"({cartela_matriz1[y][x]})"
        if x == 2 and cartela_matriz1[y][x] == d:
         cartela_matriz1[y][x] = f"({cartela_matriz1[y][x]})"
         y = y + 1 
         x = -1
        x = x + 1
        return cartela_matriz1
  
def checar_cartela2():
 x = 0
 y = 0
 if modo == 0:
  while y <= 2:

        if x == 0 and cartela_matriz2[y][x] == d:
         cartela_matriz2[y][x] = f"({cartela_matriz2[y][x]})"
        if x == 1 and cartela_matriz2[y][x] == d:
         cartela_matriz2[y][x] = f"({cartela_matriz2[y][x]})"
        if x == 2 and cartela_matriz2[y][x] == d:
         cartela_matriz2[y][x] = f"({cartela_matriz2[y][x]})"
         y = y + 1 
         x = -1
        x = x + 1
        return cartela_matriz2
  
def sortear_numero():
  x = 1
  numeros = []
  for i in range(1,31):
   numeros.append(x)
   x = x + 1

  x = 1
  numeros_c2 = []
  for i in range(1,41):
   numeros_c2.append(x)
   x = x + 1

  if modo == 0:
     d = random.choice(numeros)
     numeros.remove(d)
  if modo == 1:
     d = random.choice(numeros_c2)
     numeros_c2.remove(d)
  print(f"> Última dezena sorteada: {d}")
  return d

def imprimir_cartelar(cartela):
    print(cartela[0][0],  cartela[0][1],  cartela[0][2])
    print(cartela[1][0],  cartela[1][1],  cartela[1][2])

def imprimir_cartelad(cartela):
    print(cartela[0][0],  cartela[0][1],  cartela[0][2],  cartela[0][3])
    print(cartela[1][0],  cartela[1][1],  cartela[1][2],  cartela[1][3])
    print(cartela[2][0],  cartela[2][1],  cartela[2][2],  cartela[2][3])

def criar_cartela1(linhas, colunas):
    col1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    col2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    col3 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    col4 = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
    cartela_matriz1 = [[0 for _ in range(colunas)] for _ in range(linhas)]
    
    x = 0
    y = 0
    if modo == 0:
     while y <= 1:
        if x == 0:
         cartela_matriz1[y][x] = random.choice(col1)
         col1.remove(cartela_matriz1[y][x])
        if x == 1:
         cartela_matriz1[y][x] = random.choice(col2)
         col2.remove(cartela_matriz1[y][x])
        if x == 2:
         cartela_matriz1[y][x] = random.choice(col3)
         col3.remove(cartela_matriz1[y][x])
         y = y + 1
         x = -1
        x = x + 1
    if modo == 1:
      while y <= 2:
        if x == 0:
         cartela_matriz1[y][x] = random.choice(col1)
         col1.remove(cartela_matriz1[y][x])
        if x == 1:
         cartela_matriz1[y][x] = random.choice(col2)
         col2.remove(cartela_matriz1[y][x])
        if x == 2:
         cartela_matriz1[y][x] = random.choice(col3)
         col3.remove(cartela_matriz1[y][x])
        if x == 3:
         cartela_matriz1[y][x] = random.choice(col4)
         col4.remove(cartela_matriz1[y][x])
         y = y + 1
         x = -1
        x = x + 1
    return cartela_matriz1
def criar_cartela2(linhas, colunas):
    col1_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    col2_2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    col3_2 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    col4_2 = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
    cartela_matriz2 = [[0 for _ in range(colunas)] for _ in range(linhas)]
    
    x = 0
    y = 0
    if modo == 0:
     while y <= 1:
        if x == 0:
         cartela_matriz2[y][x] = random.choice(col1_2)
         col1_2.remove(cartela_matriz2[y][x])
        if x == 1:
         cartela_matriz2[y][x] = random.choice(col2_2)
         col2_2.remove(cartela_matriz2[y][x])
        if x == 2:
         cartela_matriz2[y][x] = random.choice(col3_2)
         col3_2.remove(cartela_matriz2[y][x])
         y = y + 1
         x = -1
        x = x + 1
    if modo == 1:
      while y <= 2:
        if x == 0:
         cartela_matriz2[y][x] = random.choice(col1_2)
         col1_2.remove(cartela_matriz2[y][x])
        if x == 1:
         cartela_matriz2[y][x] = random.choice(col2_2)
         col2_2.remove(cartela_matriz2[y][x])
        if x == 2:
         cartela_matriz2[y][x] = random.choice(col3_2)
         col3_2.remove(cartela_matriz2[y][x])
        if x == 3:
         cartela_matriz2[y][x] = random.choice(col4_2)
         col4_2.remove(cartela_matriz2[y][x])
         y = y + 1
         x = -1
        x = x + 1
    return cartela_matriz2

def exibir_cartela1():
  if modo == 0:
    criar_cartela1(num_linhasr, num_colunasr)
    imprimir_cartelar(checar_cartela1())
  if modo == 1:
    criar_cartela1(num_linhasd, num_colunasd)
    imprimir_cartelad(checar_cartela1())
  return cartela_matriz1

def exibir_cartela2():
  if modo == 0:
    criar_cartela2(num_linhasr, num_colunasr)
    imprimir_cartelar(checar_cartela2())
  if modo == 1:
    criar_cartela2(num_linhasd, num_colunasd)
    imprimir_cartelad(checar_cartela2())
  return cartela_matriz2


def escolher_modo():
    print('Indique o modo de jogo: \n0 - RÁPIDO \n1 - DEMORADO\n')
    modo = int(input())
    return modo

#programa principal
modo = escolher_modo()
cartela_matriz1 = criar_cartela1(num_linhasd, num_colunasd)
cartela_matriz2 = criar_cartela2(num_linhasd, num_colunasd)
d = sortear_numero()

jogo_acaba = False
while not jogo_acaba:
    print("Jogador 1:")
    exibir_cartela1()
    
    print("Jogador 2:")
    exibir_cartela2()
    sortear_numero()

    print("Jogador 1:")
    exibir_cartela1()

    print("Jogador 2:")
    exibir_cartela2()
    sortear_numero()
    break

    
