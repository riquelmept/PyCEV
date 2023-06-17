num = int(input("Digite um numero para ver sua tabuada: "))
print("-"*20)
for c in range(0,10):
    print("    {} x {} = {}".format(num, c, num*c))
print("-"*20)
