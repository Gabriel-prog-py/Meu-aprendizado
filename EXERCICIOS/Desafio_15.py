dias = int(input('Quantos dias pretende ficar com o carro? '))
km = float(input('Quantos Kms você rodou? '))
pago = (dias * 60) + (km * 0.15)
print(f'O valor dos dias solicitados para o aluguel e do KM rodados foram calculados e o valor a ser pago é R${pago:.2f}')
