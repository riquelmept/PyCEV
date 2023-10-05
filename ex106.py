import time
"""
Faça um minissistema que utilize o interactive help do Python

O usuário vai digitar o comando e o manual vai aparecer.

Quando o usuário digitar a palavra "FIM", o programa se encerrará!.

OBS: use cores.
"""
c = ('\033[m',
     '\033[0;30;41m',
     '\033[0;30;42m',
     '\033[0;30;43m',
     '\033[0;30;44m',
     '\033[0;30;45m',
     '\033[7:30m'
     );


def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'',4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    time.sleep(2)


def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'* tam)
    print(c[0], end='')
    time.sleep(1)


#PRINCIPAL
comando = ''
while True:
    título('SISTEMA DE AJUDA PYHelp', 2)
    comando = str(input('Funçao ou Biblioteca > '))
    if comando.upper == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!!!', 1)