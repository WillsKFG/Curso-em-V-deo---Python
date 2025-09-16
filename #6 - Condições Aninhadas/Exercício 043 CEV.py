#Exercício Python 043:
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, 

#de acordo com a tabela abaixo:
#IMC abaixo de 18,5: Abaixo do Peso
#Entre 18,5 e 25: Peso Ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade Mórbida

print("\n\t~~ CALCULADORA IMC ~~\n")

peso_str = input("Digite o peso: ")
altura_str = input("Digite a altura: ")

peso = float(peso_str.replace(',','.'))
altura = float(altura_str.replace(',','.'))

imc = peso / (altura * altura)

if imc < 18.5:
    print("\nAbaixo do Peso")
elif 18.5 <= imc < 25:
    print('\nPeso Ideal')
elif 25 <= imc < 30:
    print('\nSobrepeso')
elif 30 <= imc < 40:
    print("\nObesidade")
elif imc >= 40:
    print('\nObesidade Mórbida')

print(f"\nSeu IMC é {imc:.1f}")