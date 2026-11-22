from random import choice
n1 = str(input('Digite o nome do primeiro Aluno: '))
n2 = str(input('Digite o nome do segundo Aluno: '))
n3 = str(input('Digite o nome do terceiro Aluno: '))
n4 = str(input('Digite o nome do quarto Aluno: '))
lista = choice([n1, n2, n3, n4])
print(f'O Aluno escolhido foi {lista}')