from emoji import emojize
text = emojize(' Desafio 55 :cold_face: ')
print(f'{text:=^30}')

maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input(f'\033[33mDigite o peso da {i}º pessoa: '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'\033[32mO Maior Peso é {maior:.2f}Kg e o Menor Peso é {menor:.2f}Kg')
