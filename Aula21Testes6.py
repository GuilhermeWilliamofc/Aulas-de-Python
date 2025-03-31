def par(n = 0):
    if n % 2 == 0:
        return True
    else:
        return False
    
num = int(input('Digite um Número: '))
if par(num) == True:
    texto = 'par'
else:
    texto = 'ímpar'

print(f'O número {num} é {texto}')
