from random import shuffle
n1 = str(input('Digite o nome do primeiro Aluno: '))
n2 = str(input('Digite o nome do segundo Aluno: '))
n3 = str(input('Digite o nome do terceiro Aluno: '))
n4 = str(input('Digite o nome do quarto Aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'A ordem escolhida para a apresentação é {lista}')