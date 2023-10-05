def leia_int(entrada_usuario):
    ok = False
    value = 0
    while True:
        numero = input(f"{entrada_usuario} \n")
        if numero.isnumeric():
            value = numero
            ok = True
        else:
            print("\033[0;31mERRO! Digite um número inteiro válido!\033[m")
        if ok:
            break
    return value


n = leia_int("Digite um número:")
print(f"Você acabou de digitar o número: {n}.")