from emoji import emojize
text = emojize(' Desafio 97 :cold_face: ')
print(f'{text:=^30}')

def escreva(msg):
    tam = len(msg) + 4
    print('-' * tam)
    print(f'{msg:^{tam}}')
    print('-' * tam)

escreva('Eae')
escreva('Testezin Brabo')
escreva('Testezão com uma frase enormemente grande')
