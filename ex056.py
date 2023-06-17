sidade = 0
mdidade = 0
mh = 0
nv = ""
contm = 0
for p in range(1, 5):
    print("----- {}° PESSOA -----".format(p))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input(" Sexo [M/F]: ")).strip()
    sidade += idade

    if p == 1 and sexo in "Mm":
        mh = idade
        nv = nome
    if sexo in "Mm" and idade > mh:
        mh = idade
        nv = nome
    if sexo in "Ff" and idade < 20:
        contm += 1
mdidade = sidade/4

print("A médidade de idade do grupo é de {} anos, o homem mais velho tem {} anos e se chama {}. Ao todo, são {} mulheres com menos de 20 anos".format(mdidade, mh, nv, contm))