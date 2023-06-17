import datetime
atual = datetime.date.today().year
nascimento = int(input("Digite o ano de nascimento do atleta: "))
idade = atual - nascimento
print("O atleta tem {} anos.".format(idade))

if idade <= 9:
    print("A idade está na categoria MIRIM de até 9 anos.")
elif 9 < idade <= 14:
    print("A idade está na categoria INFANTIL de até 14 anos.")
elif 14 < idade <= 19:
    print("A idade está na categoria JÚNIOR de até 19 anos.")
elif 19 < idade <= 25:
    print("A idade está na categoria SÊNIOR de até 25 anos.")
else:
    print("A idade está na categoria MASTER para acima de 25 anos.")