distancia = int(input("\nDigite a distância de sua viagem, em KM: \n"))
if distancia <= 200:
    preco = distancia * 0.50
    print(f"O PREÇO DE SUA VIAGEM É R${preco:.2f}")
else:
    preco = distancia * 0.45
    print(f"O PREÇO DE SUA VIAGEM É R${preco:.2f}")