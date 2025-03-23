#pegar um angulo e ler o seno, cosseno e tangente
import math

ang = float(input('Digite o valor do angulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print(f"O seno de {ang}° é {sen:.2f}")
print(f"O cosseno de {ang}° é {cos:.2f}")
print(f"A tangente de {ang}° é {tan:.2f}")