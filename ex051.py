print("\033[7;30;40m=\033[m"*40)
print("\033[31m          10 TERMOS DE UMA PA\033[m")
print("\033[7;30;40m=\033[m"*40)

a = int(input("Digite o primeiro termo: "))
r = int(input("Digite a razão: "))
d = a + (10 - 1) * r

for a in range(a, d + r, r):
    print("{}".format(a), end = " => ")