from random import randint
computador = randint(0, 5)
num = int(input('estou pensando em um numero entre 0 e 5, consegue adivinhar? '))
if num == computador:
    print('Parabens você acertou!!')
else:
    print('Você errou, tento novamente')
print('=' * 10, 'FIM', '=' * 10)