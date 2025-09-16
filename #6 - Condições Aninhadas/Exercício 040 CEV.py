#Exercício Python 040:
# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO

m1 = float(input("Insira a primeira nota: "))
m2 = float(input("Insira a segunda nota: "))
media = (m1+m2)/2

if media<5:
    print(f"Sua média foi {media:.2f}, e você está REPROVADO")
elif media>7:
    print(f"Sua média foi {media:.2f}, e você está APROVADO")
elif media>=5<7:
    print(f"Sua média foi {media:.2f}, e você está de RECUPERAÇÃO")
