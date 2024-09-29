def verificar_agua_suficiente():
    try:
        agua_disponivel = float(input("Digite a quantidade de água disponível em litros: "))
        
        distancia_oasis = float(input("Digite a distância até o oásis em quilômetros: "))

        agua_necessaria = distancia_oasis * 2  

        if agua_disponivel >= agua_necessaria:
            print("A quantidade de água é suficiente para chegar ao oásis.")
        else:
            print("A quantidade de água não é suficiente para chegar ao oásis.")

    except ValueError:
        print("Por favor, insira um número válido.")

verificar_agua_suficiente()
