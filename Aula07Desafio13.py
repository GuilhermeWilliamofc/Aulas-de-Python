text = 'Desafio 13'
print(f'{text:=^30}')

salario = float(input('Digite Seu Salário - R$'))
aumento = 0.15
novosalario1 = salario*aumento
novosalario2 = salario+novosalario1
print(f'O Seu salário de R${salario:.2f} com um aumento de 15%, passa a valer R${novosalario2:.2f}')
