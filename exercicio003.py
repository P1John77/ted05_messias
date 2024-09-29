def adivinhar_animal():

    tipo_animal = input("Seu animal favorito é um mamífero ou um réptil? (digite 'mamífero' ou 'réptil'): ").strip().lower()

    if tipo_animal == 'mamífero':
        print("Seu animal favorito pode ser um cachorro!")
    elif tipo_animal == 'réptil':
        print("Seu animal favorito pode ser uma tartaruga!")
    else:
        print("Resposta inválida! Por favor, digite 'mamífero' ou 'réptil'.")

adivinhar_animal()
