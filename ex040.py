n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))

media = (n1 + n2)/2
print("Com as notas {:.1f} e {:.1f}, a média foi de {:.1f}".format(n1, n2, media))

if media < 5.0:
    print("O aluno está REPROVADO")
elif 5.0 < media <= 6.9:
    print("O aluno está de RECUPERAÇÃO")
else:
    print("O aluno está APROVADO")