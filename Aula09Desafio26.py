from emoji import emojize
text = emojize(' Desafio 26 :cold_face: ')
print(f'{text:=^30}')

amarelo = ('\033[33m')
ciano = ('\033[36m')
roxo = ('\033[35m')

frase = input(f'{amarelo}Digite uma frase: ').strip()
frase = frase.lower()
frasecount = frase.count('a')
fraseprim_a = frase.find('a')
fraselast_a = frase.rfind('a')
print(f'{roxo}A Letra A aparece:\n{ciano}{frasecount} vezes na frase\nA primeira vez na posição {fraseprim_a+1}\nA última vez na posição {fraselast_a+1}')
