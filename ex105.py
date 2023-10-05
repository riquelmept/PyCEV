def notas(*n, sit=False):
    """Funcão para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param situacao: valor opcional, indicando se deve ou não adicionar a situação
    :return dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r["total"] = len(n)  # total
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)

    if sit:
        if r["média"] >= 7:
            r["situacao"] = "BOM"
        elif r["média"] >= 5:
            r["situacao"] = "RAZOÁVEL"
        else:
            r['situacao'] = 'RUIM'
    return r


# Programa principal:
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)