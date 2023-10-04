def área(l, c):
    a = larg * comp
    print(f'A área de um terreno com {larg} x {c} é de {comp}m²')


print("CALCULO DA AREA DO TERRENO")
print('-'*20)

larg = float(input('Largura: (m) '))
comp = float(input('Comprimento: (m) '))

área(larg, comp)