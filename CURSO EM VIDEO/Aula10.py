# nome = str(input('Digite seu nome: '))
# if nome == 'Gabriel':
#     print('Que nome bonito você tem!')
# else:
#     print('Seu nome é então normal!')
# print(f'Bom dia, {nome}')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'Sua meida foi {m:.1f}')
if m == 10:
    print('Você é um exemplo de Aluno, PARABENS!!!')
elif m >= 6:
    print('Sua media foi boa!!, PARABENS!!!!!!')
else:
    print('Sua media foi ruim, ESTUDE MAIS!')
