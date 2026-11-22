temperatura = float(input('Qual a temperatura em Celsius? '))
farenheit = (temperatura * 9/5) + 32
Kelvin = (temperatura - 32) * 5 / 9 + 273.15
print(f'A temperatura de {temperatura}°C corresponde a {farenheit:.1f}°F')