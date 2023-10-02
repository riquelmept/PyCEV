cont = ("zero", "um", "dois", "três", "quatro",
        "cinco", "seis", "sete","oito", "nove",
        "dez", "onze", "doze", "treze", "catorze",
        "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
while True:
    núm = int(input('Digite um númetro entre 0 e 20:' ))
    if núm < 0 or núm > 20:
       print('Você digitou um número fora do range permitido, tente novamente. \n', end = '') 
    resp = ' '
    if 0 <= núm <= 20:
        print(f'Você digitou o número {cont[núm]}')
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if resp == "N":
        break
