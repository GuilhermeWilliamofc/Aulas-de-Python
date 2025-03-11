from emoji import emojize
text = emojize(' Aula 09 - Testes :smiling_face_with_horns: ')
print(f'{text:=^30}')

frase = str('Curso em Vídeo Python')
print((frase[1:].title()))
print(len(frase))
print(frase.replace('Curso', 'Guilherme'))
print('Python' in frase)
print(frase.find('Guilherme'))
