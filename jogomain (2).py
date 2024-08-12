import random
def jogo_de_adivinhacao():
    numero_secreto = random.randint(1, 100) # Gera um número aleatorio entre 1 e 100
    tentativas = 0

    # Descrição do Jogo
    print("Bem - vindo ao Jogo de Adivinhação!")
    print("O objetivo do jogo é advinhar um numero aleatorio entre 1 e 100.")
    print("Voçê recebera dicas se o palpite for muito alto ou muido baixo.")
    print("Boa sorte!\n")

    print("Tente adivinhar o numero entre 1 e 100.")
    while True:
        try:
            chute = int(input("Digite seu palpite:")) # Solicita um palpite do jogador
            tentativas += 1
            if chute < 1 or chute > 100:
               print("Por favor, digite um numero entre 1 e 100.") # Verifica se o palpite esta no intervalo permitido
               continue

            if chute > numero_secreto:
                print("Muito alto! Tente novamente.")
            elif chute > numero_secreto:
                print("Muito baixo! Tente novamente.")
            else:
                print(f"Parabens! Voce adivinhou o numero em {tentativas} tentativas.")
                break # O Jogo termina quando o numero é adivinhado
        except ValueError:
            print("Entrada invalida! Por favor, digite um numero.")
# Chama a função para iniciar o jogo
jogo_de_adivinhacao()
