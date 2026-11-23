radar = int(input('Em qual velocidade o carro passou? '))
if radar <= 80:
    print('Você está no limite da velocidade!')
else:
    velocidade = (radar - 80) * 7
    print(f'Você foi multado e o valor da multa é de R${velocidade:.2f}')