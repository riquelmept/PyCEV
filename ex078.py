listnum = []
mai = 0
men = 0
for c in range (0,5):
    listnum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listnum[c]
    else:
        if listnum[c] > mai:
            mai = listnum [c]
        if listnum[c] < men:
            men = listnum[c]
print('='*30)
print(f'Você digitou os valores {listnum}')
print(f'O maior valor digitado foi {mai} nas posições')
for i, v in enumerate(listnum):
    if v == mai:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {men} nas posições ', end='')
for i, v in enumerate(listnum):
    if v == men:
        print(f'{i}...', end='')
print()