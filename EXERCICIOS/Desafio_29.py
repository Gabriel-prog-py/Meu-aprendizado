radar = int(input('Em qual velocidade o carro passou? '))
limite = 80
if radar <= 80:
    print('Você está no limite da velocidade!')
else:
    velocidade = (radar - limite) * 7
    print(f'Você foi multado e o valor da multa é de R${velocidade:.2f}')