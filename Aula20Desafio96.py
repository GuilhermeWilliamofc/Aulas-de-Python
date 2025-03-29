from emoji import emojize
text = emojize(' Desafio 96 :cold_face: ')
print(f'{text:=^30}')

def texto(msg):
    print('-' * 30)
    print(f'{msg:^30}')
    print('-' * 30)

def area(a, b):
    tot = a * b
    print(f'A área de um terreno {a:.1f} x {b:.1f} é de {tot:.1f}m².')


texto('Controle de Terrenos')

a = float(input('Largura (M): '))
b = float(input('Comprimento (M): '))
area(a, b)
