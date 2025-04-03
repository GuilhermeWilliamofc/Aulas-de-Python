try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('\033[31mTivemos um problema com os tipos de dados que você digitou\033[m')
except ZeroDivisionError:
    print('\033[31mNão é possível dividir um número por zero\033[m')
except KeyboardInterrupt:
    print('\033[31mO usuário preferiu não informar os dados\033[m')
except Exception as erro:
    print(f'\033[31mO erro encontrado foi {erro.__cause__}\033[m')
else:
    print(f'O resultado é {r:.2f}')
finally:
    print('Volte sempre muito obrigado')
