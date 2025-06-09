#Exercício Python 036:

#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print("\n\t--- SIMULAÇÃO EMPRÉSTIMO BANCÁRIO ---\n")

casa = float(input("Insira o Valor da Casa: R$"))
salario = float(input("Insira o Valor do Salário do(a) Comprador(a): R$"))
anos = int(input("Insira Quantos Anos Será de Financiamento: "))

prestacao = casa / (anos*12)
minimo = salario * 30/100

print(f"\nPara pagar uma casa de R${casa:.2f} em {anos} anos\na prestação será de {anos}x de R${prestacao:.2f}\n")

if prestacao <= minimo:
    print("O empréstimo pode ser CONCEDIDO!!!")
else:
    print("Empréstimo NEGADO!!!")

print("\n\t--- FIM DO PROGRAMA ---")
