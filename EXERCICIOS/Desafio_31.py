distancia = int(input('Qual a distanciar que sera percorrida na viagem? '))
preco_ate_200 = 0.50
preco_acima_de_200 = 0.45
if distancia <= 200:
    soma = distancia * preco_ate_200
    print(f'O valor da passagem sera de R${soma:.2f}')
else:
    soma_2 = distancia * preco_acima_de_200
    print(f'O valor da passagem acima de 200KM sera R${soma_2:.2f}')