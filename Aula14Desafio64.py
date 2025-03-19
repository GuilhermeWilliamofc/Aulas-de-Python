from emoji import emojize
text = emojize(' Desafio 64 :cold_face: ')
print(f'{text:=^30}')

num = 0
soma = 0
conta = 0
while not num == 999:
    num = int(input('Digite um número: '))
    soma += 1
    conta += num

print(f'Durante a Execução do Programa {soma-1} número(s) foram digitados sendo que a soma entre eles deu {conta-999}')
