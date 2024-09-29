def determinar_vencedor():
    ataque_guerreiro1 = float(input("Digite o ataque do Guerreiro 1: "))
    defesa_guerreiro1 = float(input("Digite a defesa do Guerreiro 1: "))

    ataque_guerreiro2 = float(input("Digite o ataque do Guerreiro 2: "))
    defesa_guerreiro2 = float(input("Digite a defesa do Guerreiro 2: "))

    total_guerreiro1 = ataque_guerreiro1 + defesa_guerreiro1
    total_guerreiro2 = ataque_guerreiro2 + defesa_guerreiro2

    if total_guerreiro1 > total_guerreiro2:
        print("O Guerreiro 1 é o vencedor!")
    elif total_guerreiro2 > total_guerreiro1:
        print("O Guerreiro 2 é o vencedor!")
    else:
        if defesa_guerreiro1 > defesa_guerreiro2:
            print("O Guerreiro 1 é o vencedor por desempate!")
        elif defesa_guerreiro2 > defesa_guerreiro1:
            print("O Guerreiro 2 é o vencedor por desempate!")
        else:
            print("Empate! Ambos guerreiros têm habilidades iguais.")

determinar_vencedor()
