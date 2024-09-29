def calcular_bonus():
    try:
        missoes_completadas = int(input("Digite o número de missões completadas pelo cavaleiro: "))

        if missoes_completadas > 10:
            bonus = 100
        elif 5 <= missoes_completadas <= 10:
            bonus = 50
        else:
            bonus = 10

        print(f"O bônus do cavaleiro é de {bonus} moedas de ouro.")

    except ValueError:
        print("Por favor, insira um número válido para o número de missões.")

calcular_bonus()
