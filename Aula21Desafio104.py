from emoji import emojize
text = emojize(' Desafio 104 :cold_face: ')
print(f'{text:=^30}')

def leiaint(n):
    num = ' '
    while not num.isnumeric() == True:
        num = input(n)
        if num.isnumeric() == False:
            print('\033[31mErro! Digite um número inteiro válido')
    return int(num)


n = leiaint('\033[33mDigite um número: ')
print(f'\033[32mVocâ acabou de digitar o número {n}')
