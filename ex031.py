distância = float(input(print("Digite a distância da sua viagem em quilômetros")))

if distância > 200.00:
    vt = distância * 0.5
    print("Sua viajem será de {} km, o valor total será de R${:.2f}! Boa viajem!".format(distância, vt))
else:
    vt = distância * 0.45
    print("Sua viajem será de {} km, o valor total será de R${:.2f}! Boa viajem!".format(distância, vt))
