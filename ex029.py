velocidade = int(input(print("Qual a velocidade do carro?")))
permitido = 80
if velocidade < 80:
    print("Velocidade permitida!")
else:
    print("Multado! VOcê excedeu o limite permitido que era de 80Km/h")
    multa = (velocidade - permitido) * 7
    print("Você deve pagar uma multa de R${},00".format(multa))

print("Tenha um bom dia! Dirija com segurança!")
