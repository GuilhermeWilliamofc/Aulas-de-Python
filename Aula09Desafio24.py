from emoji import emojize
text = emojize(' Desafio 24 :cold_face: ')
print(f'{text:=^30}')

cidade = input('Digite o Nome de uma Cidade: ').strip
if cidade:
    cidade = cidade.lower().split()
    if cidade[0] == 'santo':
        print('A Cidade começa com Santo')
    else:
        print('A Cidade não começa com Santo')
