estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy())
for e in brasil:
    #for k, v in e.items():
        #print(f'O campo {k} tem valor {v}')
    for v in e.values():
        print(f'{v}')