resposta = 's'
pares = 0
tot = 0
while resposta == 's':
    num = int(input('Digite um valor: ')) 
    resposta = input('Quer Continuar? [S/N] ').lower()
    tot += 1
    if num % 2 == 0:
        pares += 1
print(f'Durante a execução do programa {tot} número(s) foram digitados, sendo eles {pares} número(s) pares')
print('Fim do Programa')
