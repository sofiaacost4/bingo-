import random

#Aluna: Sofia Costa Kunzler
#Professor: Alexandre
#Turma: Infoweb 1

#Checa se o número sorteado está em alguma cartela e, se estiver, o marca com [] na cartela
def checar_cartela(cartela, num_sorteado):
    for i in range(len(cartela["cartela"])):
        for j in range(len(cartela["cartela"][0])):
            if cartela["cartela"][i][j] == num_sorteado:
                cartela["escolhidos"][i][j] = True

    
#Sorteia um número aleatório, sem repetição.
def sortear_numero(modo, numeros_sorteados, numeros):
    while True:
        d = random.choice(numeros)
        numeros.remove(d)
        if d not in numeros_sorteados:
            numeros_sorteados.append(d)
        return d

#Imprime a cartela
def imprimir_cartela(cartela):
    for linha in cartela:
        print(" ".join(f"{num:2}" for num in linha))

#Cria a cartela com base no modo escolhido
def criar_cartela(modo, jogador):
    col1 = list(range(1, 11))
    col2 = list(range(11, 21))
    col3 = list(range(21, 31))
    col4 = list(range(31, 41))

    if modo == 0:
        colunas, linhas = 3, 2
    else:
        colunas, linhas = 4, 3

    cartela_matriz = [[0 for _ in range(colunas)] for _ in range(linhas)]

    for y in range(linhas):
        for x in range(colunas):
            if x == 0:
                cartela_matriz[y][x] = random.choice(col1)
                col1.remove(cartela_matriz[y][x])
            elif x == 1:
                cartela_matriz[y][x] = random.choice(col2)
                col2.remove(cartela_matriz[y][x])
            elif x == 2:
                cartela_matriz[y][x] = random.choice(col3)
                col3.remove(cartela_matriz[y][x])
            elif x == 3:
                cartela_matriz[y][x] = random.choice(col4)
                col4.remove(cartela_matriz[y][x])

    return {
        "jogador": jogador,
        "cartela": cartela_matriz,
        "escolhidos": [[False] * colunas for _ in range(linhas)]
    }

#Mostra a cartela no programa
def exibir_cartela(cartela):
    print(f"Jogador {cartela['jogador']}:")
    for linha, marcado in zip(cartela['cartela'], cartela['escolhidos']):
        print(" ".join(f"[{num:2}]" if m else f"{num:2}" for num, m in zip(linha, marcado)))
    print('\033[35m❣\033[m ',"- " * 20,'\033[35m❣\033[m ')

#Checa se algum jogador marcou todos os números da cartela e venceu
def checar_se_venceu(cartela):
    return all(all(row) for row in cartela["escolhidos"])

#Função do jogo principal
def jogo():
    print("Escolha o modo de jogo:")
    print("0 - MODO RÁPIDO")
    print("1 - MODO DEMORADO")
    
    while True:
            modo = int(input("Digite 0 ou 1: "))
            if modo == 0 or modo == 1:
                break
            else:
                print("Indique um modo de jogo válido!")
    
    num_jogadores = 2 if modo == 0 else 4
    cartelas = [criar_cartela(modo, f + 1) for f in range(num_jogadores)]
    numeros_sorteados = []
    numeros = list(range(1, 31)) if modo == 0 else list(range(1, 41))

    while True:
        input("Pressione ENTER para continuar o jogo")
        num_sorteado = sortear_numero(modo, numeros_sorteados, numeros)
        print(f"=> Último número sorteado: {num_sorteado}")
        print(f"Números sorteados até agora: {sorted(numeros_sorteados)}")

        for cartela in cartelas:
            checar_cartela(cartela, num_sorteado)
            exibir_cartela(cartela)
            if checar_se_venceu(cartela):
                print(f"\033[35mJogador {cartela['jogador']} é o vencedor!\033[m（っ＾▿＾）")
                return

jogo()