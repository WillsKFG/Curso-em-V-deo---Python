import random
numero = random.randint(0, 5)
print("\nAdivinhe o número que estou pensando entre 0 e 5\n")

while True:
    numero_user = int(input("Digite um número entre 0 e 5: "))
    if numero == numero_user:
        print("Parabéns! Você acertou!")
        break
    elif numero > numero_user:
        print("Você errou! O número que pensei é maior que o seu.")
    elif numero < numero_user:
        print("Você errou! O número que pensei é menor que o seu.")

