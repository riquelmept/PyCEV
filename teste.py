from utilidadescev import moeda
from utilidadescev import dado

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')
print(moeda.resumo(p, 20, 12))
p1 = dado.leiaDinheiro('Digite o preço: R$')
