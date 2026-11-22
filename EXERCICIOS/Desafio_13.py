salario_atual = float(input('Qual o salario do atual do funcionario? R$'))
aumento = salario_atual * 0.15
salario_final = salario_atual + aumento
print(f'O salario do funcionario era é R${salario_atual:,.2f} e ele ganhou um amento de R${aumento:,.2f} e seu salario passou a ser R${salario_final:.2f}')