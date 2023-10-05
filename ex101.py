import datetime
def voto(birthyear):
    ano_atual = datetime.date.today().year
    age = ano_atual - birthyear
    if age < 16:
        return f"Com {age} anos de idade: VOTO NEGADO"
    elif age < 18 or age >= 65:
        return f"Com {age} anos de idade: VOTO OPCIONAL"
    elif age < 65:
        return f"Com {age} anos de idade: VOTO OBRIGATÓRIO"


ano_nasc = int(input("Em qual ano você nasceu? \n"))
print(voto(ano_nasc))