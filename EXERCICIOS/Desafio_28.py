from random import randint
computador = randint(0, 5)
print('-=-' * 20)
num = int(input('estou pensando em um numero entre 0 e 5, consegue adivinhar? '))
print('-=-' * 20)
if num == computador:
    print('Parabens você acertou!!')
else:
    print(f'Eu ganhei! Eu pensei no numero {computador} e não no numero {num}!')
print('-=-' * 10, 'FIM', '-=-' * 10)