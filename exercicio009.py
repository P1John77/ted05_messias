def escolher_feitiço():
    try:
        escolha = int(input("Escolha um feitiço:\n1 - Fogo\n2 - Água\n3 - Terra\nDigite o número correspondente: "))

        match escolha:
            case 1:
                print("Você escolheu o feitiço de Fogo!")
            case 2:
                print("Você escolheu o feitiço de Água!")
            case 3:
                print("Você escolheu o feitiço de Terra!")
            case _:
                print("Escolha inválida! Por favor, escolha 1, 2 ou 3.")

    except ValueError:
        print("Por favor, insira um número válido.")

escolher_feitiço()
