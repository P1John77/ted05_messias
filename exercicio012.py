def escolher_arma():
    espada_ataque = float(input("Digite o poder de ataque da espada: "))
    espada_durabilidade = float(input("Digite a durabilidade da espada: "))

    arco_ataque = float(input("Digite o poder de ataque do arco: "))
    arco_durabilidade = float(input("Digite a durabilidade do arco: "))

    lança_ataque = float(input("Digite o poder de ataque da lança: "))
    lança_durabilidade = float(input("Digite a durabilidade da lança: "))

    armas_adequadas = []

    if espada_ataque > 50 and espada_durabilidade > 70:
        armas_adequadas.append("Espada")
        
    if arco_ataque > 50 and arco_durabilidade > 70:
        armas_adequadas.append("Arco")
        
    if lança_ataque > 50 and lança_durabilidade > 70:
        armas_adequadas.append("Lança")

    if armas_adequadas:
        print(f"As armas adequadas são: {', '.join(armas_adequadas)}.")
    else:
        print("Nenhuma arma atende aos requisitos. O herói deve buscar uma nova arma.")

escolher_arma()
