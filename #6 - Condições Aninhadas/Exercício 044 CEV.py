#Exercício Python 044:
# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:

#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço formal
#3x ou mais no cartão: 20% de juros

def dinheiro():
    desconto = preco * 0.1
    vista = preco - desconto
    print(f"O valor total que você deve pagar é de R${vista:.2f}")
    escolha = input("\nDeseja consultar outra forma de pagamento? (S/N)\n").lower()
    if escolha == 's':
        menu()
    elif escolha == 'n':
        print(f"\n--- FIM DO PROGRAMA ---\n")
        exit()
    else:
        print("Opção Inválida, tente novamente")

def cartao():
    desconto = preco - 0.05

def menu():
    print(f'''
    [1] - À vista dinheiro/cheque
    [2] - À vista no cartão
    [3] - Em até 2x no cartão
    [4] - Em 3x ou mais no cartão

    [5] - Alterar Valor -> (Valor Atual: R${preco:.2f})

    [6] - Sair do programa''')

print("\n\t--- Loja do Wills ---\n")
preco_str = input("Digite o preço R$")
preco = float(preco_str.replace(',','.'))
menu()

while True:
    opcao = int(input("\nEscolha uma opção: "))
    if opcao == 1:
        dinheiro()
    elif opcao == 2:
        cartao()
    elif opcao == 3:
        cartao2x()
    elif opcao == 4:
        cartao3x()
    elif opcao ==5:
        
    elif opcao == 6:
        print(f"\n--- FIM DO PROGRAMA ---\n")
        break
    else:
        print("Opção Inválida, Tente Novamente.")




