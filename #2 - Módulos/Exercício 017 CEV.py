#calcular hipotenusa
import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = math.hypot(co, ca)
print(f'A hipotenusa é {h:.2f}')