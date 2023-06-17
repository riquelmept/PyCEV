import datetime

atual = datetime.date.today().year
contmaior = 0
contmenor = 0

for peoples in range (1, 8):
    dt = int(input("Em que ano a {}° pessoa nasceu? ".format(peoples)))
    age = atual - dt
    
    if age >= 21:
        contmaior += 1
    else:
        contmenor += 1

print("Ao todo tivemos {} pessoas maiores de idade".format(contmaior))
print("Também, ao todo tivemos {} pessoas menores de idade".format(contmenor))