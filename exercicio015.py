def verificar_portal():
    energia = float(input("Digite a energia disponível (%): "))
    coordenadas = input("Digite as coordenadas de destino (ex: 'x,y'): ")
    tempo = float(input("Digite o tempo ajustado (em segundos): "))

    energia_correta = energia > 80
    coordenadas_certas = coordenadas.count(',') == 1 and all(coord.strip().replace('-', '').replace('.', '').isdigit() for coord in coordenadas.split(','))
    tempo_correto = tempo >= 0

    if energia_correta and coordenadas_certas and tempo_correto:
        print("Portal de viagem no tempo ativado com sucesso!")
    else:
        if not energia_correta:
            print("Problema: Energia insuficiente. Deve estar acima de 80%.")
        if not coordenadas_certas:
            print("Problema: Coordenadas de destino estão incorretas. Formato correto: 'x,y'.")
        if not tempo_correto:
            print("Problema: Tempo ajustado deve ser maior ou igual a 0 segundos.")

verificar_portal()
