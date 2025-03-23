#Sorteador de Ordem de apresentação dos alunos
aluno1 = str(input("Digite o nome do(a) primeiro(a) aluno(a): ").capitalize())
aluno2 = str(input("Digite o nome do(a) segundo(a) aluno(a): ").capitalize())
aluno3 = str(input("Digite o nome do(a) terceiro(a) aluno(a): ").capitalize())
aluno4 = str(input("Digite o nome do(a) quarto(a) aluno(a): ").capitalize())
lista = [aluno1, aluno2, aluno3, aluno4]

import random
sorteio = random.shuffle(lista)

print("A lista de ordem a sorteada é:")
print(lista)