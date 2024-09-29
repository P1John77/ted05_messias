def calcular_media(notas):
    return sum(notas) / len(notas)

def selecionar_governante():
    notas_candidato1 = list(map(float, input("Digite as notas do Candidato 1 (separadas por espaço): ").split()))
    notas_candidato2 = list(map(float, input("Digite as notas do Candidato 2 (separadas por espaço): ").split()))
    notas_candidato3 = list(map(float, input("Digite as notas do Candidato 3 (separadas por espaço): ").split()))

    media1 = calcular_media(notas_candidato1)
    media2 = calcular_media(notas_candidato2)
    media3 = calcular_media(notas_candidato3)

    print(f"Média do Candidato 1: {media1:.2f}")
    print(f"Média do Candidato 2: {media2:.2f}")
    print(f"Média do Candidato 3: {media3:.2f}")

    if media1 > media2 and media1 > media3:
        print("O Candidato 1 é o próximo governante.")
    elif media2 > media1 and media2 > media3:
        print("O Candidato 2 é o próximo governante.")
    elif media3 > media1 and media3 > media2:
        print("O Candidato 3 é o próximo governante.")
    else:
        print("Houve um empate entre os candidatos.")

selecionar_governante()
