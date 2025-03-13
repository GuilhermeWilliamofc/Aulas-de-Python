text = 'Desafio 08'
print(f'{text:=^30}')

metro = float(input('\033[33mDigite um valor em metro - '))
cm = metro*100
mm = metro*1000
print(f'\033[36mo Valor de {metro}m em centímetro é {cm}cm e em milimetro é {mm}mm')
# se eu não quiser nenhuma casa decimal adiciono :.0f no código
