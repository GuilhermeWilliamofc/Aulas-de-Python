from emoji import emojize
text = emojize(' Desafio 80 :cold_face: ')
print(f'{text:=^30}')

num = []

for i in range(1, 6):
    lista = int((input(f'Digite o {i}º Número: ')))
    if lista < num.index(num(max)):
        num.insert(num.index(num(max)), lista)
    num.append(lista)

