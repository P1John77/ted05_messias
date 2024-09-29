def desafio_porta(numero_porta):
    match numero_porta:
        case 1:
            return "Você encontrou um dragão feroz! Prepare-se para a batalha."
        case 2:
            return "Uma tempestade magica se aproxima! Use suas habilidades para sobreviver."
        case 3:
            return "Você se depara com um enigma antigo. Resolva-o para avançar."
        case 4:
            return "Um tesouro está escondido atrás dessa porta! Mas cuidado com os guardiões."
        case 5:
            return "Você encontrou um portal para outra dimensao! O que você fara agora?"
        case _:
            return "Porta inválida! Escolha um número de 1 a 5."

numero_porta = int(input("Escolha uma porta (1 a 5): "))
resultado = desafio_porta(numero_porta)
print(resultado)
