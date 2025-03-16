#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salario, com 15% de aumento.

print("Vamos ver seu novo salário!")

salarioantigo = float(input("Primeiro, insira seu salário atual "))

salarionovo = salarioantigo * 1.15

print("seu novo salário é: R${:.2f}".format(salarionovo))