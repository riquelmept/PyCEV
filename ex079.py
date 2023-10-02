numbers = list()
while True:
    n = int(input("Digite um valor: "))
    if n not in numbers:
        numbers.append(n)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado! Não será adicionado.")
    r = str(input("Quer continuar? [S/N]"))
    if r in 'Nn':
        break
print('='*30)
numbers.sort()
print(f'Você digitou os valores {numbers}')