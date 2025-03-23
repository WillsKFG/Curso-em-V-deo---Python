#escolher 1 entre 4 alunos para um trabalho
import random

aluno1 = str(input('Digite o nome do primeiro aluno: ').capitalize())
aluno2 = str(input("Digite o nome do segundo aluno: ").capitalize())
aluno3 = str(input("Digite o nome do terceiro aluno: ").capitalize())
aluno4 = str(input("Digite o nome do quarto aluno: ").capitalize())

alunos = [aluno1, aluno2, aluno3, aluno4]
sorteado = random.choice(alunos)

print(f'O(a) aluno(a) sorteado é {sorteado}')