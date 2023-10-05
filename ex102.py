def fatorial(num, show=False):

    fatorial = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end="")
            if c > 1:
                print(" x ", end="")
            else:
                print(" = ", end="")
        fatorial *= c
    return fatorial


numero = int(input("Digite um número par saber o fatorial: \n"))
print(fatorial(numero, show=True))
help(fatorial)