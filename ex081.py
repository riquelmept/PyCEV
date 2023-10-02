values = []
while True:
    values.append(int(input("Digite um valor: ")))
    resp = str(input("Quer continuar? [S/N] "))
    if resp in 'Nn':
        break
print('='*30)
print(f'Você digitou {len(values)} elementos.')
values.sort(reverse=True)
print(f'Os valores em ordem decrescente são {values}')
if 5 in values:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')