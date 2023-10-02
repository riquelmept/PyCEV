equa = str(input('Digite a equação: '))
pilha = []

for symb in equa:
    if symb == '(':
        pilha.append('(')
    elif symb == ')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha)==0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')