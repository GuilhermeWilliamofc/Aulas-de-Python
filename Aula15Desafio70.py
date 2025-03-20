from emoji import emojize
text = emojize(' Desafio 70 :cold_face: ')
print(f'{text:=^30}')

resposta = 's'
total = caro = menortot = menor = 0
barato = ''
loja = '\033[33m     Lojas Gw'
print('\033[33m='*30)
print(f'{loja: ^30}')
print('\033[33m='*30)
print('')

while resposta == 's':
    nome = input('\033[36mDigite o Nome do Produto: ').title()
    preco = float(input('\033[35mDigite o Valor do Produto: R$'))
    total += preco

    if preco > 1000:
        caro += 1
    if menortot == 0:
        barato = nome
        menor = preco
    if preco < menor:
        barato = nome
        menor = preco

    menortot += 1
    resposta = input('\033[33mDeseja Continuar? [S/N]: ').lower().strip()[0]

print(f'\033[32mCompra Finalizada!\nO Total da Compra foi de R${total:.2f}\n{caro} Produto(s) Custam Mais de R$1000.00\nO Produto Mais Barato é {barato} que Custa R${menor:.2f}')
