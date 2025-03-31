from emoji import emojize
text = emojize(' Desafio 103 :cold_face: ')
print(f'{text:=^30}')

def ficha():
    global nome
    global gols

    if nome == '' or nome.isnumeric() == True:
        nome = '<desconhecido>'
    
    if gols == '' or gols.isnumeric() == False or gols.isspace() == True:
        gols = 0
    else:
        gols = int(gols)
     
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')


nome = input('Nome do Jogador: ').title().strip()
gols = input('Número de Gols: ').strip()
ficha()
