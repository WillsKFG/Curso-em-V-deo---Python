#Escreva um Programa que leia um valor cm metros 2 0 exiba conyertido em centimetros e milimetro.

m= int(input('digite seu valor em metros: '))

cm= m*100
mm= m*1000

print('em centímetros, {}m mede {}cm'.format(m,cm))
print("e em milímetros, {}m mede {}mm".format(m,mm))