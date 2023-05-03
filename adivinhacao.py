import random
def jogar():
    print("*****************************")
    print('Bem vindo ao jogo adivinhação')
    print("*****************************")

    # round(random.random() * 100) aqui random.random() funciona entre 0.0 e 1.0 e round arredonda pra mais
    numero_secreto = random.randrange(1, 101)
    # esse  já arredonda e define de 1 até  < 101, ou seja 100
    total_de_tentativas = 0
    pontos = 1000
    print(numero_secreto)
    nivel = 0
    while nivel < 1 or nivel > 3:
        print("Escolha seu nível de dificuldade!")
        print("(1) Fácil (2) Médio (3) Difícil")
        nivel = int(input("Nível: "))

        if nivel == 1:
            total_de_tentativas = 20
        elif nivel == 2:
            total_de_tentativas = 10
        elif nivel == 3:
            total_de_tentativas = 3
        else:
            print("Você deve digitar um numero entre 1 , 2 ou 3!")

    rodada = 1

    # for rodada in range(1, total_de_tentativas+1)

    while rodada <= total_de_tentativas:
        # interpolação de string
        # se fosse um numero float seria {:.2f} para duas casas decimais
        # antes do ponto coloca a quantidade de caracteres ex {:7.2f}
        # no inteiro só há numeros antes do ponto ex data '{:2d}/{:2d}'.format(31,12)
        # a forma mais atual  é a que foi aplicada. o format ta no f no início do literals

        print(f'Tentativa {rodada} de {total_de_tentativas}')
        chute = int(input("Digite um número entre um e cem: "))

        print("Você digitou: ", chute)
        if chute < 1 or chute > 100:
            print("Você deve digitar um numero entre 1 e 100!")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Voce acertou! Vc fez {:.2f} pontos.".format(pontos))
            break
        else:
            pontos_perdidos = abs(chute - numero_secreto) / 3  # abs() ignora o sinal, devolve um número absoluto
            pontos = pontos - pontos_perdidos
            if maior:
                print("Você errou, chute é maior!")
                if rodada == total_de_tentativas:
                    print(f"O número secreto era {numero_secreto}. Você fez {pontos}")
            elif menor:
                print("Você errou, chute é menor!")
                if rodada == total_de_tentativas:
                    print(f"O número secreto era {numero_secreto}. Você fez {pontos}")

        rodada += 1
    print("Fim do Jogo")
if __name__ == "__main__":
    jogar()