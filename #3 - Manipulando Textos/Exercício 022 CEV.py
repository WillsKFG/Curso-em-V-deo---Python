# Exercício 022 - CEV - Curso em Vídeo Python
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input("----- Insira seu  nome completo: ----- \n"))
print('')
primeiro_nome = nome.split()[0]

print('---------------------------------------')
print('------- analisando seu nome... --------')
print('---------------------------------------\n')

print('* o nome em maiúsculo é:',nome.upper(),';')
print('* o nome em minúsculo é:',nome.lower(),';')
print('* o nome completo possui ao todo:',len(nome)-nome.count(' '),'letras;')
print('* o primeiro nome tem:',len(primeiro_nome), 'letras.\n')
print('---------------------------------------')
print('----------- FIM DO PROGRAMA -----------')
print('---------------------------------------')