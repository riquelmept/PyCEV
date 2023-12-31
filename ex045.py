from random import choice, randint, shuffle
from time import sleep

print('{:=^40}'.format( ' JO KEN PO '))
print('{:=^40}\n'.format( ' THE GAME '))
print('Sua Opcoes:')
print(' [ 0 ] PEDRA')
print(' [ 1 ] PAPEL')
print(' [ 2 ] TESOURA')
user = ['PEDRA', 'PAPEL', 'TESOURA']
play = int(input('Qual e a sua jogada?: '))
if play < 0 or play >= 3:
    print('\033[1;30;41mOPCAO INVALIDA. INSIRA OPCAO ENTRE 0 E 2\033[m')
    exit()

nome = user[play]

print('{:*^20}'.format(' JO... '))
sleep(1)
print('{:*^20}'.format(' KEN... '))
sleep(1)
print('{:*^20}\n'.format(' PO !! '))

pc = ['PEDRA', 'PAPEL', 'TESOURA']
escolhido = pc.index(choice(pc))
nome_pc = pc[escolhido]

if escolhido == play:
    msg = 'EMPATE! JOGUE NOVAMENTE'
elif (escolhido == 0 and play == 2) or (escolhido == 2 and play == 1) or (escolhido == 1 and play == 0):
    msg = 'COMPUTADOR GANHA!! VOCE \033[7;31mPERDEU\033[m :('
else:
    msg = 'VOCE \033[7;30mGANHOU\033[m !! PARABENS!!'

print('-='*20)
print('Sua Jogada: \033[4;36m{}\033[m'.format(nome))
print('*'*40)
print('Jogada do Computador: \033[4;33m{}\033[m'.format(nome_pc))
print('-='*20)
print(msg)