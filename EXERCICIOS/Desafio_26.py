frase = str(input('Digite sua frase: ')).upper().strip()
quantidade = frase.count('A')
inicio = frase.find('A') +1
final = frase.rfind('A') +1
print(f'A quantidade de Letras A da frase é {quantidade}')
print(f'A primeira posição da Letra A da frase é {inicio}')
print(f'A ultima posição que a letra A aparece na frase e na posição {final} ')
