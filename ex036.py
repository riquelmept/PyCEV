valor = float(input("Valor da casa: R$"))
salario = float(input("Salário do comprador: R$"))
anos = int(input("Quantos anos de finaciamento? "))

parcela = valor/(anos*12)
mínimo = salario * 0.3

if parcela >= mínimo:
    print("A parcela ficou inviável para pagamento com sua renda atual!")
    print(parcela)
else:
    print("Empréstimo Aprovado!!! A parcela será de: R${:.2f}".format(parcela))
    print("Parabéns pela sua aquisição!")
