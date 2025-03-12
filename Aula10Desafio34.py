from emoji import emojize
text = emojize(' Desafio 34 :cold_face: ')
print(f'{text:=^30}')

salario = float(input('Digite seu salário: '))
if salario > 1250.00:
    aumento1 = salario * 0.10 + salario
    conta1 = aumento1 - salario
    print(f'Seu salário de R${salario:.2f} com aumento será R${aumento1:.2f} (10% de Aumento ou R${conta1:.2f})')
else:
    aumento2 = salario * 0.15 + salario
    conta2 = aumento2 - salario
    print(f'Seu salário de R${salario:.2f} com aumento será R${aumento2:.2f} (15% de Aumento ou R${conta2:.2f})')
