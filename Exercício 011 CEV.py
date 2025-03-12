#Faça um programa que leia a largura e a altura de uma parede em metros. calcule a area e a quantidade de tinta necessaria para pinta-la, sobendo que cada litro de tinta. pinta uma Area de 2m².
  
print("Olá! Vamos medir a área de sua parede para sabermos quantos litros de tintas serão necessários")

h = int(input("Primeiro, insira a altura de sua parede em metros "))
b = int(input("Agora, insira a largura de sua parede, também em metros "))
        
wall = h * b

litros = wall/2

print("A área de sua parede é: {}m², e você irá precisar de {} litros de tinta para pinta-lá".format(wall, litros))
