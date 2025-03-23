from emoji import emojize
text = emojize(' Desafio 83 :cold_face: ')
print(f'{text:=^30}')

expr = input('\033[33mDigite a expressão: ')
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('\033[32mSua expressão está válida!')
else:
    print('\033[31mSua expressão está inválida!')
