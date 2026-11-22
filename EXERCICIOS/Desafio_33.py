primeiro_numero = int(input('Digite o primeiro numero: '))
segundo_numero = int(input('Digite o segundo numero: '))
terceiro_numero = int(input('Digite o terceiro numero: '))
maior = primeiro_numero
menor = primeiro_numero

if segundo_numero > maior:
    maior = segundo_numero
if segundo_numero < menor:
    menor = segundo_numero

if terceiro_numero > maior:
    maior = terceiro_numero
if terceiro_numero < menor:
    terceiro_numero = menor
print(f'O maior numero é {maior}')
print(f'O menor numero é {menor}')



