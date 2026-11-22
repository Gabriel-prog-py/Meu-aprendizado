salario = float(input('Qual o seu salario? R$ '))
if salario > 1250:
    aumento = salario * 0.10
    salario_final = salario + aumento
    print(f'Seu salario atual é de R${salario:.2f} e seu aumentou foi de 10%, agora seu salario é de R${salario_final:.2f}')
else:
    salario <= 1250
    aumento = salario * 0.15
    salario_final = salario + aumento
    print(f'Seu salario atual é de R${salario:.2f} e seu aumentou foi de 15%, agora seu salario é de R${salario_final:.2f}')