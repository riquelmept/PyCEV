larg = float(input("largura da parede: "))
alt = float (input("Altura da parede: "))
area = larg * alt
print("A sua parede tem a dimensao de {}x{} e sua area e de {}m²".format(larg, alt, area))
tinta =  area/2
print("Para pintar essa parede, voce precisara de {}l de tinta".format(tinta))