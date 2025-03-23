#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
  #Considere
  #USS1.00 = RS3.27

reais = float(input("quantos reais vc possui na carteira? "))

dolar = reais / 3.27

print(f"com R${reais:.2f} você pode comprar US${dolar:.2f}")