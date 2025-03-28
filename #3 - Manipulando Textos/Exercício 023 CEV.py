# Exercício 023 - CEV - Curso em Vídeo Python
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

while True:
   numero = int(input("\nDigite um número inteiro entre 0 e 9999:\n".center(largura := 40)))

   if numero < 0 or numero > 9999:
    print("Número inválido! Tente novamente.".center(largura))
   else:
       break

print('='*50)
print(f"Analisando o número {numero}...".center(largura))
print('='*50)

milhar = (numero // 1000) % 10
centena = (numero // 100) % 10
dezena = (numero // 10) % 10
unidade = numero % 10

largura = 40

print(f"Milhar:  {milhar}".center(largura))
print(f"Centena: {centena}".center(largura))
print(f"Dezena:  {dezena}".center(largura))
print(f"Unidade: {unidade}".center(largura))

print('='*50)
print(f"FIM DO PROGRAMA".center(largura))
print('='*50)
