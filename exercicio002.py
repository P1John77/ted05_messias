def verificar_liga():
    try:
       
        ferro = float(input('Digite a quantidade de ferro em kg: '))
        ouro = float(input('Digite a quantidade de ouro em kg: '))

        if ferro < 0 or ouro < 0:
            print('As quantidades de ferro e ouro devem ser não negativas.')
            return

        total_liga = ferro + ouro

        if total_liga > 0:
            porcentagem_ferro = (ferro / total_liga) * 100

            print(f'A porcentagem de ferro na liga é: {porcentagem_ferro:.2f}%')

            if porcentagem_ferro >= 70:
                print('A porcentagem de ferro é suficiente para a armadura.')
            else:
                print('A porcentagem de ferro não é suficiente para a armadura.')
        else:
            print('A quantidade total da liga deve ser maior que zero.')

    except ValueError:
        print('Por favor, insira valores numéricos válidos.')

verificar_liga()
