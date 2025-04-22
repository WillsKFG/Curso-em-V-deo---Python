print("-="*20, "Analisador de Triângulos", "-="*20)
print("Digite as medidas dos três lados do triângulo:")
a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

if a + b > c and a + c > b and b + c > a:
    print("As medidas formam um triângulo.")
    if a == b == c:
        print("O triângulo é equilátero.")
    elif a == b or a == c or b == c:
        print("O triângulo é isósceles.")
    else:
        print("O triângulo é escaleno.")
else:
    print("As medidas não formam um triângulo.")
print("-="*20, "FIM", "-="*20)