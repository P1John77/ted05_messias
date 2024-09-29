def calcular_valor_moedas():
    try:
        moedas_1_real = int(input("Digite a quantidade de moedas de 1 real: "))
        moedas_50_centavos = int(input("Digite a quantidade de moedas de 50 centavos: "))
        moedas_25_centavos = int(input("Digite a quantidade de moedas de 25 centavos: "))

        total = (moedas_1_real * 1.00) + (moedas_50_centavos * 0.50) + (moedas_25_centavos * 0.25)

        print(f"O valor total que o colecionador tem é: R$ {total:.2f}")
        
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

calcular_valor_moedas()

