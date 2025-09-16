#Exercício Python 041:
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JÚNIOR
#Até 25 anos: SÊNIOR
#Acima de 25 anos: MASTER

from datetime import  date

ano_nascimento = int(input("Insira o ano de nascimento: "))

ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print(f"\nO atleta possui {idade} anos\n")

if idade <= 9:
    print("Classificação: MIRIM\n")
elif idade <= 14:
    print("Classificação: INFANTIL\n")
elif idade <= 19:
    print("Classificação: JÚNIOR\n")
elif idade <= 25:
    print("Classificação: SÊNIOR\n")
else:
    print("Classificação: MASTER\n")

