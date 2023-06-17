salário = float(input("Digite seu salário: "))

#Checa o salário comparando aos parâmetros para o aumento.
if salário < 1250:
    novosalário = salário + (salário * 0.10)
    acréscimo = salário * 0.10
else:
    novosalário = salário + (salário * 0.15)
    acréscimo = salário * 0.15

print("O salário informado de R${:.2f}, terá um acréscimo de R${:.2f}, totalizando R${:.2f}".format(salário, acréscimo, novosalário))
