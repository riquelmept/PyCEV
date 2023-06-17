import datetime
atual = datetime.date.today().year
ano_nasc = int(input("Ano de nascimento: "))
idade = atual - ano_nasc
liminf = 18
limsup = 45
print(("Quem nasceu em {} tem {} anos em {}.".format(ano_nasc, idade, atual)))
if idade > limsup:
    print("A idade está acima de {} anos, o cidadão não pode se alistar.".format(limsup))
elif idade < liminf:
    print("A idade está abaixo de {} anos, o cidadão não pode se alistar.".format(liminf))
else:
    print("A idade está entre {} e {} anos, o cidadão pode realizar seu alistamento.".format(liminf, limsup))