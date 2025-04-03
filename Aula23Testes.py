try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'\033[31mProblema encontrado foi {erro.__class__}\033[m')
else:
    print(f'O resultado é {r:.2f}')
finally:
    print('Volte sempre muito obrigado')
