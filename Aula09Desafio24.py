from emoji import emojize
text = emojize(' Desafio 24 :cold_face: ')
print(f'{text:=^30}')

cidade = input('\033[33mDigite o Nome de uma Cidade: ').lower().strip().split()
if cidade:
    if cidade[0] == 'santo':
        print('\033[32mA Cidade começa com Santo')
    else:
        print('\033[31mA Cidade não começa com Santo')
