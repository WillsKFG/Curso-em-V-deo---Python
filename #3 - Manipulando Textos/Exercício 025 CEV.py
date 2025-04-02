#Exercício 025 - CEV - Curso em Vídeo Python
# Crie um programa que leia o nome completo de uma pessoa, mostrando se ela possui Silva no nome

nome = str(input("insira seu nome: ")).strip()
print (f"Seu nome tem silva? {'silva' in nome.lower()}")