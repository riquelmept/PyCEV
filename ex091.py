import random, time, operator

jogo = {'Jogador1': random.randint(1, 6),
        'Jogador2': random.randint(1,6),
        'Jogador3': random.randint(1, 6),
        'Jogador4': random.randint(1, 6)}

ranking = list()
print('Valores sorteados:')

for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    time.sleep(1)
    
ranking = sorted(jogo.items(), key=lambda item: item[1], reverse=True)
print('='*30)
print('  ==  RANKING DOS JOGADORES  ==')

for i, v in enumerate(ranking):
    print(f'   {i+1} {v[0]} com {v[1]}.')
    time.sleep(1)