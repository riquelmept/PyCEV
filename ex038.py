import time

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
print("Um momento...")
time.sleep(3.5)
if n1 > n2:
    print("O primeiro número {} é maior que {}.".format(n1, n2))
elif n1 < n2:
    print("O segundo número {} é maior que {}.".format(n2, n1))
else:
    print("Os números {} e {} são iguais.".format(n1, n2))