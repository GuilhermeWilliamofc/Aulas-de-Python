text = 'Desafio 14'
print(f'{text:=^30}')

celsius = float(input('\033[33mInforme a temperatura em °C - '))
fahrenheit = celsius*1.8+32
conversao = print(f'\033[34mA temperatura de {celsius}°C corresponde a {fahrenheit}°F!')
