def ficha(nome_jogador, numero_gols):
    return f"O jogador {nome_jogador.upper()} fez {numero_gols} gols."


nome = str(input("Nome do jogador: \n"))
if len(nome) == 0:
    nome = "<desconhecido>"

gols = str(input("Número de gols: \n"))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0


print(ficha(nome, gols))