def calcular_distancia():
    try:
        x = int(input('Digite o número de passos para o norte (X): '))
        y = int(input('Digite o número de passos para o leste (Y): '))
        
        distancia_total = x + y
        
        print(f'A distância total que o pirata precisa percorrer é: {distancia_total} passos.')
    except ValueError:
        print('insira números inteiros válidos.')

calcular_distancia()
