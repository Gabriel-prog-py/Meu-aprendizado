from math import sqrt, hypot
cateto_oposto = float(input('Informe o cateto oposto: '))
cateto_adjacente = float(input('informe o cateto adjacente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print(f'A hipotenusa mede {hipotenusa:.2f}')

#hypot é usado para calcular a Hypotenusa