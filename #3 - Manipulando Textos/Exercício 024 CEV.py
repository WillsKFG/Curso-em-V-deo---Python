# Exercício 024 - CEV - Curso em Vídeo Python
# # Crie um programa que pergunte o nome de uma cidade e diga se ela começa ou não com o nome "Santo".

print('='*10,'VAMOS VER SE SUA CIDADE COMEÇA COM SANTO NO NOME','='*10)


cidade = str(input('\n Em que cidade você nasceu?\n')).strip()
print('')
print(cidade[:5].upper() == 'SANTO')
print('')
print('='*26,'FIM DO PROGRAMA','='*26)
print('')