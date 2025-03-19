resposta = 's'
pares = 0
impares = 0
tot = 0
while resposta == 's':
    num = int(input('Digite um valor: ')) 
    resposta = input('Quer Continuar? [S/N] ').lower()
    tot += 1
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f'Durante a execução do programa {tot} número(s) foram digitados, sendo eles {pares} número(s) pares e {impares} número(s) ímpares')
print('Fim do Programa')
