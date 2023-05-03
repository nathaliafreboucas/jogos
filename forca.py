import random

def imprime_apresentacao():

    print("*****************************")
    print("Bem vindo ao jogo da Forca")
    print("*****************************")
def carrega_palavra_secreta():
    # abrindo arquivos de palavras
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        palavras.append(linha.strip())

    arquivo.close()

    palavra_aleatoria = random.randrange(0, len(palavras))
    palavra_secreta = palavras[palavra_aleatoria]


    return palavra_secreta
def inicializa_lacunas(palavra_secreta):
    # for letra in palavra_secreta:
    #   letras_certas.append("_")

    # é o mesmo que isso logo abaixo
    # preenchendo os espaços da palavra secreta com linhas

    letras_certas = ["_" for letra in palavra_secreta]
    print(letras_certas)
    return letras_certas
def insere_chute():
    chute = input("Qual letra?: ").lower().strip()
    return chute
def posiciona_chute_correto(palavra_secreta, chute, letras_certas):
    posicao = 0
    # percorrendo a palavra para colocar as letras na posição correta
    for letra in palavra_secreta:
        if chute == letra:  # entrada fica minusculos e sem espaços respectivamente
            letras_certas[posicao] = letra
        posicao = posicao + 1
    print(letras_certas)
    return letras_certas

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("     _______________         ")
    print("    /              \       ")
    print("   /                \      ")
    print("/\/                  \/\  ")
    print("\ |   XXXX     XXXX  | /   ")
    print(" \|   XXXX     XXXX  |/     ")
    print("  |   XXX       XXX  |      ")
    print("  |                  |      ")
    print("  \__      XXX     __/     ")
    print("   |\      XXX    / |       ")
    print("   | |           |  |        ")
    print("   | I I I I I I I  |        ")
    print("   |  I I I I I I   |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
def desenha_forca(erros,letras_certas):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print(letras_certas)

def jogar():

    imprime_apresentacao()
    palavra_secreta = carrega_palavra_secreta()
    letras_certas = inicializa_lacunas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    #enquanto não enforcou e não acertou
    while not enforcou and not acertou:
        print("Jogando...")
        chute = insere_chute()

        #se o chute tem na palavra
        if chute in palavra_secreta:
          posiciona_chute_correto(palavra_secreta, chute, letras_certas)
          # verifica se existem espaços com linha para determinar resultado do jogo
          if "_" not in letras_certas:
              imprime_mensagem_vencedor()
              break
        else:
            #contando a quantidade de erros
            erros = erros + 1
            tentativas = 7
            desenha_forca(erros,letras_certas)
        
            tentativa = tentativas - erros
            print(f"Você errou! Ainda restam {tentativa} tentativas")

            if erros == 7:
                imprime_mensagem_perdedor(palavra_secreta)
                break

    print("Fim de Jogo!")

if __name__ == "__main__": #ajuda a executar independente do arquivo 'jogos'
    jogar()