#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5 porcento de desconto.

valor = float(input("insira o valor do produto em reais "))

desconto = valor * 0.95

print("seu produto com 5% de desconto fica por R${}". format(desconto))