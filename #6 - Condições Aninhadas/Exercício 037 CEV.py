#Exercício Python 037:

# Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal.

print("\n\t--- CONVERSOR NÚMERO INTEIRO ---\n")
num = int(input("Digite um número inteiro para converter: "))
while True:
    
    print('''
    ESCOLHA UMA OPÇÃO:
    [1] - BINÁRIO
    [2] - HEXADECIMAL
    [3] - OCTAL
    ''')
    escolha = int(input(f"\nDeseja converter {num} para qual?\n"))

    if escolha ==1:
        print(f"O número {num} em BINÁRIO é: {bin(num)[2:]}")
        break
    elif escolha==2:
        print(f"O número {num} em HEXADECIMAL é: {hex(num)[2:]}")
        break
    elif escolha==3:
        print(f"O número {num} em OCTAL é igual a: {oct(num)[2:]}")
        break
    else:
        print("Opção Inválida, Tente Novamente!")
