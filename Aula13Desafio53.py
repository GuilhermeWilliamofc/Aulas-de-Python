from emoji import emojize
text = emojize(' Desafio 53 :cold_face: ')
print(f'{text:=^30}')

frase = input('\033[33mDigite uma frase: ')
dividir = frase[::-1]
edicao1 = frase.lower() 
edicao1_2 = edicao1.replace(' ', '')
edicao1_3 = dividir.lower().replace(' ', '')
edicao2 = frase.title().strip()
if edicao1_3 == edicao1_2:
    print(f'\033[32mA Frase "{edicao2}" é um palindromo pois invertida é "{edicao1_3.title()}"')
else:
    print(f'\033[31mA Frase "{edicao2}" não é um palindromo pois invertida é "{dividir.title()}"')
