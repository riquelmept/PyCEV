brasileiro = ('Botafogo', 'Bragantino', 'Grêmio', 'Palmeiras', 'Flamengo', 'Fluminense',
              'Atlético-MG', 'Athletico-PR', 'Fortaleza', 'São Paulo', 'Cuiabá',
              'Cruzeiro', 'Corinthians', 'Internacional', 'Santos', 'Vasco',
              'Goiás', 'Bahia', 'América-MG', 'Coritiba')
print('='*60)
print(f'Lista de times do Brasileirão: {brasileiro}')
print('='*60)
print(f'Os 5 primeiros são: {brasileiro[0:5]}')
print('='*60)
print(f'Os 4 últimos são: {brasileiro[-4:]}')
print('='*60)

while True:
    time = input(str('Digite o time que deseja saber a colocação: '))
    if time not in brasileiro:
        print(f'O time {time} não está classificado na série A do campeonato.')
        print('='*60)
        break

    print(f'O time {time} está na {brasileiro.index(time)+1}° posição')
    
    resp = ' '
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if resp == "N":
        break

print('='*60)