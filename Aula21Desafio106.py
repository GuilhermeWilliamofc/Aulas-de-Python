from emoji import emojize
text = emojize(' Desafio 106 :cold_face: ')
print(f'{text:=^30}')

def pyhelp():
    while True:
        from time import sleep
        sleep(1)
        print('\033[30;42m-' * 40)
        print('\033[30;42mSistema de Ajuda - PyHelp')
        print('-' * 40)
        sleep(1)
        cmd = ' '
        while cmd.isalnum() == False:
            cmd = input('\033[mFunção ou Biblioteca (Escreva fim para sair): ').lower().strip()
        if cmd == 'fim':
            break
        print('\033[4;33;44m-' * 40)
        print(f'\033[4;33;44mAcessando o Manual do comando \'{cmd}\'') 
        # \' para aparecer aspas na mensagem
        print('\033[4;33;44m-' * 40)
        sleep(1)
        print('\033[107;98m')
        help(cmd)
    print('\033[41;97m-' * 40)
    print('\033[41;97mAté Logo!')
    print('\033[41;97m-' * 40)
    sleep(1)

if __name__ == "__main__":
    pyhelp()
