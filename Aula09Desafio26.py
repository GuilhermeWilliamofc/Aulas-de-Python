from emoji import emojize
text = emojize(' Desafio 26 :cold_face: ')
print(f'{text:=^30}')

frase = input('Digite uma frase: ')
frase = frase.lower()
frasecount = frase.count('a')
fraseprim_a = frase.find('a')
fraselast_a = frase.rfind('a')
print(f'A Letra A aparece:\n{frasecount} vezes na frase\nA primeira vez na posição {fraseprim_a+1}\nA última vez na posição {fraselast_a+1}')
