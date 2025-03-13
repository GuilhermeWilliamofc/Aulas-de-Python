text = 'Desafio 10'
print(f'{text:=^30}')

real = float(input('\033[33mDigite um Valor em Real (R$) - '))
dolar = real/3.27
print(f'\033[32mCom {real} Real/is você pode comprar {dolar:.2f} Dolár/es')

# o dolár hoje tá R$ 5.79, mas o exercicio quer que eu considere como R$ 3.27