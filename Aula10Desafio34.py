from emoji import emojize
text = emojize(' Desafio 34 :cold_face: ')
print(f'{text:=^30}')

amarelo = ('\033[33m')
verde = ('\033[32m')

salario = float(input('\033[36mDigite seu salário: \033[32mR$ '))
if salario > 1250.00:
    aumento1 = salario * 0.10 + salario
    conta1 = aumento1 - salario
    print(f'Seu salário de {amarelo}R${salario:.2f}{verde} com aumento será {amarelo}R${aumento1:.2f}{verde} ({amarelo}10%{verde} de Aumento ou {amarelo}R${conta1:.2f}{verde})')
else:
    aumento2 = salario * 0.15 + salario
    conta2 = aumento2 - salario
    print(f'Seu salário de {amarelo}R${salario:.2f}{verde} com aumento será {amarelo}R${aumento2:.2f}{verde} ({amarelo}15%{verde} de Aumento ou {amarelo}R${conta2:.2f}{verde})')
