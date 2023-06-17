s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        cont += 1

print("A soma dos números múltiplos de 3 de 1 até 500 é de {}, foram contabilizados {} valores".format(s,cont))
 