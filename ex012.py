preco = float(input("Qual e o preç do produto? R$"))
NOVO = preco - (preco *(5/100))
print("O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}".format(preco, NOVO))