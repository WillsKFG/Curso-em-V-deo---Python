#exercicio 006
#crie um algoritmo que leia um número e mostra o seu dobro, triplo e raíz quadrada 

num = int(input('insira seu número '))

x2 = num * 2
x3 = num * 3
rqua = num ** 0.5

print('''seu número é {}
o dobro de {} é {}
o triplo de {} é {}
e a raíz quadrada de {} é {:.2f}'''.format (num,num,x2,num,x3,num,rqua))