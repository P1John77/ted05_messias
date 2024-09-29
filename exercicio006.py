def comparar_dragoes():
    try:
        distancia_dragao1 = float(input("Digite a distância percorrida pelo primeiro dragão (em metros): "))
        tempo_dragao1 = float(input("Digite o tempo que o primeiro dragão levou (em segundos): "))

        distancia_dragao2 = float(input("Digite a distância percorrida pelo segundo dragão (em metros): "))
        tempo_dragao2 = float(input("Digite o tempo que o segundo dragão levou (em segundos): "))

        velocidade_dragao1 = distancia_dragao1 / tempo_dragao1
        velocidade_dragao2 = distancia_dragao2 / tempo_dragao2

        print(f"A velocidade do primeiro dragão é: {velocidade_dragao1:.2f} m/s")
        print(f"A velocidade do segundo dragão é: {velocidade_dragao2:.2f} m/s")

        if velocidade_dragao1 > velocidade_dragao2:
            print("O primeiro dragão é mais rápido.")
        elif velocidade_dragao1 < velocidade_dragao2:
            print("O segundo dragão é mais rápido.")
        else:
            print("Ambos os dragões têm a mesma velocidade.")

    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

comparar_dragoes()
