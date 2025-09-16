#Exercício Python 038:

# Escreva um programa que leia dois números inteiros e compare-os.
# mostrando na tela uma mensagem:
#  - O primeiro valor é maior
#  - O segundo valor é maior
#  - Não existe valor maior, os dois são iguais

print("\n\t -- COMPARADOR DE NÚMEROS --\n")
n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
if n1>n2:
    print("o PRIMEIRO número é maior\n")
elif n1<n2:
    print("o SEGUNDO número é maior\n")
else:
    print("os números são IGUAIS.\n")