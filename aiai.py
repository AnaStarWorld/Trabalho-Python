# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|".join(linha))
        print("-" * 5)

# Função para verificar se há um vencedor
def verificar_vencedor(tabuleiro, jogador):
    # Verificar linhas
    for linha in tabuleiro:
        if linha.count(jogador) == 3:
            return True

    # Verificar colunas
    for col in range(3):
        if tabuleiro[0][col] == tabuleiro[1][col] == tabuleiro[2][col] == jogador:
            return True

    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True

    return False

# Função para verificar se há empate
def verificar_empate(tabuleiro):
    for linha in tabuleiro:
        if " " in linha:
            return False
    return True

# Função principal do jogo
def jogo_da_velha():
    # Inicializar o tabuleiro
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    
    # Jogadores
    jogador_atual = "X"

    while True:
        imprimir_tabuleiro(tabuleiro)
        print(f"Vez do jogador {jogador_atual}")

        # Entrada do jogador
        linha = int(input("Escolha a linha (0, 1, 2): "))
        coluna = int(input("Escolha a coluna (0, 1, 2): "))

        # Verificar se a posição está disponível
        if tabuleiro[linha][coluna] != " ":
            print("Posição já ocupada. Tente novamente.")
            continue

        # Colocar a jogada no tabuleiro
        tabuleiro[linha][coluna] = jogador_atual

        # Verificar se o jogador venceu
        if verificar_vencedor(tabuleiro, jogador_atual):
            imprimir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu!")
            break

        # Verificar empate
        if verificar_empate(tabuleiro):
            imprimir_tabuleiro(tabuleiro)
            print("Empate!")
            break

        # Alternar entre os jogadores
        jogador_atual = "O" if jogador_atual == "X" else "X"

# Executar o jogo
jogo_da_velha()
