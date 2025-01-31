import random
#Aluna: Sofia Costa
#Turma: Infoweb 1 ano
#Professor: Alexandre

#constantes (não devem mudar ao decorrer do jogo)

num_linhasr = 2
num_linhasd = 3
num_colunasr = 3
num_colunasd = 4

def checar_cartela(cartela, numero):
    for i in range(len(cartela["cartela"])):
        for j in range(len(cartela["cartela"][0])):
            if cartela["cartela"][i][j] == numero:
                cartela["marcados"][i][j] = True

#etapa 3: sorteia um número aleatório sem repetir
def sortear_numero(modo, numeros_sorteados):
  x = 1
  numeros_sorteados = []
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
     if d not in numeros_sorteados:
        numeros_sorteados.append(d)
  elif modo == 1:
     d = random.choice(numeros_c2)
     numeros_c2.remove(d)
     if d not in numeros_sorteados:
        numeros_sorteados.append(d)
  print(f"> Última dezena sorteada: {d}")
  return d


#etapa 1: gerar a cartela 
def imprimir_cartelar(cartela):
    print(cartela[0][0],  cartela[0][1],  cartela[0][2])
    print(cartela[1][0],  cartela[1][1],  cartela[1][2])

def imprimir_cartelad(cartela):
    print(cartela[0][0],  cartela[0][1],  cartela[0][2],  cartela[0][3])
    print(cartela[1][0],  cartela[1][1],  cartela[1][2],  cartela[1][3])
    print(cartela[2][0],  cartela[2][1],  cartela[2][2],  cartela[2][3])

def criar_cartela(modo, jogadores):
    col1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    col2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    col3 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    col4 = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
    if modo == 0:
       colunas, linhas = 3, 2
    elif modo == 1:
       colunas, linhas = 4, 3
    cartela_matriz = [[0 for _ in range(colunas)] for _ in range(linhas)]
    
    x = 0
    y = 0
    z = 0
    if modo == 0:
     z = 1
    elif modo == 1:
     z = 2
    while y <= z:
        if x == 0:
         cartela_matriz[y][x] = random.choice(col1)
         col1.remove(cartela_matriz[y][x])
        if x == 1:
         cartela_matriz[y][x] = random.choice(col2)
         col2.remove(cartela_matriz[y][x])
        if x == 2:
         cartela_matriz[y][x] = random.choice(col3)
         col3.remove(cartela_matriz[y][x])
        if x == 3:
         cartela_matriz[y][x] = random.choice(col4)
         col4.remove(cartela_matriz[y][x])
         y = y + 1
         x = -1
        x = x + 1
    return cartela_matriz, {'jogadores': jogadores, 'cartela': cartela_matriz}

def exibir_cartela(cartela):
    print(f"Jogador {cartela['jogador']}")
    for linha, marcado in zip(cartela['cartela'], cartela['marcados']):
        print(" ".join(f"({n})" if m else f"{n}" for n, m in zip(linha, marcado)))
    print("-" * 20)

def verificar_vencedor(cartela):
    return all(all(row) for row in cartela["marcados"])

def jogo():
    print("Escolha o modo de jogo:")
    print("0 - MODO RÁPIDO")
    print("1 - MODO DIFÍCIL")
    
    while True:
        try:
            modo = int(input("Digite 0 ou 1: ").strip())
            if modo in [0, 1]:
                break
            else:
                print("Entrada inválida! Digite 0 para MODO RÁPIDO ou 1 para MODO DIFÍCIL.")
        except ValueError:
            print("Entrada inválida! Digite um número válido.")
    
    num_jogadores = 2 if modo == 0 else 4
    cartelas = [criar_cartela(modo, i + 1) for i in range(num_jogadores)]
    numeros_sorteados = []
    
    while True:
        input("Pressione ENTER para continuar")
        num_sorteado = sortear_numero(modo, numeros_sorteados)
        print(f"=> Última desena sorteada: {num_sorteado}")
        print(f"Dezenas sorteadas até o momento: {numeros_sorteados}")
        
        for cartela in cartelas:
            checar_cartela(cartela_matriz, num_sorteado)
            exibir_cartela(cartela)
            if verificar_vencedor(cartela):
                print(f"Jogador {cartela['jogador']} é o vencedor!")
                return
jogo()
