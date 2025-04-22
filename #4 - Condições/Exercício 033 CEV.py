n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite mais um número: "))

if n2 < n1 and n2 < n3:
    menor = n2
elif n1 < n2 and n1 < n3:
    menor = n1
else:
    menor = n3
    
if n2 > n1 and n2 > n3:
    maior = n2
elif n1 > n2 and n1 > n3:
    maior = n1
else:
    maior = n3
print(f'O menor número é {menor} e o maior número é {maior}')
print('FIM DO PROGRAMA!')
