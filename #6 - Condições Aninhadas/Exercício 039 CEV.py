#Exercício Python 039:
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar
# ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

ano_atual = date.today().year
ano_nascimento = int(input("ano de nascimento: "))
idade = ano_atual - ano_nascimento

print(f"Quem nasceu em {ano_nascimento} tem {idade} anos em {ano_atual}\n")

if idade > 18:
    saldo = idade-18
    if saldo == 1:
        print(f"Já passou do tempo de se alistar\nVocê deveria ter se alistado a {saldo} ano!\n")
    else:
        print(f"Já passou do tempo de se alistar\nVocê deveria ter se alistado a {saldo} anos!\n")
elif idade < 18:
    saldo = 18-idade
    if saldo == 1:
        print(f"Ainda não passou do tempo de se alistar\nVocê deverá se alistar daqui {saldo} ano!\n")
    else:
        print(f"Ainda não passou do tempo de se alistar\nVocê deverá se alistar daqui {saldo} anos!\n")
else:
    print("Já está na hora de se alistar, procure uma junta militar imediatamente!!!\n")