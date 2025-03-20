from emoji import emojize
text = emojize(' Desafio 73 :cold_face: ')
print(f'{text:=^30}')

times = ('Botafogo','Palmeiras','Flamengo','Fortaleza','Internacional','São Paulo','Corinthians','Bahia','Cruzeiro','Vasco da Gama','Vitória','Atlético Mineiro','Fluminense','Grêmio','Juventude','Bragantino','Athletico-PR','Criciúma','Atlético Goianiense','Cuiabá')

print('Os Times do Brasileirão São:')
print(times)

print('\nOs Primeiros 5 Colocados São:')

for mostrar in range(0, 5):
    print(f'{times[mostrar]} em {mostrar + 1}º')

print('\nOs Últimos 4 Colocados São:')

for mostrar2 in range(-4, 0):
    print(f'{times[mostrar2]} em {mostrar2 + 21}º')

print('\nOs Times em Ordem Alfabética:')

print(sorted(times))

print('\nE o Flamengo está', end = ' ')
mengao = times.index('Flamengo')
print(f'em {mengao + 1}º')
