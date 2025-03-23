from emoji import emojize
text = emojize(' Desafio 80 :cold_face: ')
print(f'{text:=^30}')

lista = []

for c in range(1, 6):
    n = int((input(f'Digite o {c}º Número: ')))
    if c == 1:
        lista.append(n)
        print('Adicionado ao começo da lista...')
    elif n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1

print(f'Os valores digitados em ordem foram: {lista}')
