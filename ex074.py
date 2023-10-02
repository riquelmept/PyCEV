import random
números = ((random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10)))

print("Os valores sorteados foram: ", end = '')
for n in números:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(números)}')
print(f'\nO menor valor sorteado foi {min(números)}')