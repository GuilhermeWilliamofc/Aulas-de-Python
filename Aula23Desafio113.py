from Modulos.Aula22Desafio107Modulos.titulo import titulo

titulo(113)

def leiaint(texto):
    while True:
        try:
            n = int(input(texto))
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar esse número\033[m')
            n = 0
            break
        except:
            print('\033[31mErro: Por favor, digite um número inteiro válido\033[m')
        else:
            break
    return n


def leiafloat(texto):
    while True:
        try:
            n = float(input(texto))
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar esse número\033[m')
            n = 0
            break
        except:
            print('\033[31mErro: Por favor, digite um número real válido\033[m')
        else:
            break
    return n

n_int = leiaint('Digite um Inteiro: ')
n_float = leiafloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {n_int} e o real foi {n_float}')
