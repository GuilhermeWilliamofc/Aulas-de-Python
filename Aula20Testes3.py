def contador(* num):
    tam = len(num)
    print(f'Recebi {tam} Valores, São eles: ', end= '')
    for valor in num:
        print(f'{valor} ', end= '')
    print('')

contador(2, 4, 6, 8, 10)
contador(3, 6, 9)
contador(5, 10)

# esse def vira uma tupla e pode fazer tudo oq se faz com tuplas como o uso do for