import time

def lin():
  print('-' * 30)
def maior(*args):
    cont = maior = 0
    print("Analisando os valores passados...")
    print("Valores informados: ", end="")
    
    for i in args:
        print(f"{i} ", end="")
        time.sleep(0.2)
    print("")
    print(f"Ao todo são {len(args)} valores.")
    
    if len(args) == 0:
      print(f"O maior valor informado foi {maior}")
    else:
      maior = max(args)
      print(f"O maior valor informado foi {maior}")
    lin()
    print("")

#Programa principal
lin()
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()