pessoas = {'Nome': 'Gustavo', 'Sexo': 'M', 'Idade': '22'}
print(pessoas)
print(pessoas['Nome'])
print(pessoas['Idade'])
print(pessoas['Sexo'])
# quando for usar f string usar aspas duplas se n vai dar erro
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
del pessoas['Sexo']
pessoas['Nome'] = 'Leandro'
pessoas['Peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')