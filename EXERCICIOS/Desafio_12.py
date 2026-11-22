preco_original = float(input('Digite o valor do produto: '))
desconto = preco_original * 0.05
valor_final = preco_original - desconto
print(f'O valor original do produto é R${preco_original} e seu valor com desconto de 5% ficou R${valor_final:.2f}')