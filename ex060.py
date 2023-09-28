x = int(input("Digite o número que deseja o fatorial: "))
n = x
f = 1

print("Obtendo parâmetros para {}! = ".format(x), end = " ")

while n> 0:
    print("{}".format(n), end = " ")
    print(" x " if n > 1 else " = ", end = " ")
    f *= n
    n -= 1
print("{}".format(f))