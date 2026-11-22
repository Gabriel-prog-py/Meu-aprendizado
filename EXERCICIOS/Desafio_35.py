reta_a = int(input('Digite o comprimento da reta A: '))
reta_b = int(input('Digite o comprimento da reta B: '))
reta_c = int(input('Digite o comprimento da reta C: '))
if reta_a + reta_b > reta_c and reta_a + reta_c > reta_b and reta_b + reta_c > reta_a:
    print(f'comprimentos {reta_a}, {reta_b}, {reta_c}, formam um triangulo')
else:
    print(f'os comprimentos {reta_a}, {reta_b}, {reta_c}, NÃO forma um triangulo')
