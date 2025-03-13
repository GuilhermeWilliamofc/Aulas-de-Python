text = 'Desafio 11'
print(f'{text:=^30}')

largura = float(input('\033[33mDigite a Largura em metros - '))
altura = float(input('Digite a Altura em metros - '))
area = largura*altura
tinta = area/2
print(f'\033[32mA sua parede de {altura}m de altura e {largura}m de largura tem a área de {area}m²\ne precisaria de aproximadamente {tinta} litros de tinta')
