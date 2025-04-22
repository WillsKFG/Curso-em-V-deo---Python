vel = int(input("\nO CARRO ESTÁ A QUANTOS KM/H?\n"))

if vel > 80:
    print('! ! ! -MULTADO, EXCESSO DE VELOCIDADE- ! ! !')
    multa = (vel - 80) * 7
    print(f'Você deve pagar R${multa:.2f} de multa!')

else:
    print('Você está dentro do limite de velocidade!')
    print('Tenha um bom dia! Dirija com segurança!')
