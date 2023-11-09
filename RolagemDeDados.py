import random

D = int(input("Quantas faces tem o seu dado?"))
mod = int(input("Adicione o seu modificador (adicione 0 se não houver)"))

if D not in {4, 6, 8, 10, 12, 20, 100}:
    print("Escolha um dado valido")
    vant = 0
else:
    vant = input("Deseja rodar com vantagem (V), desvantagem (D) ou normal (N)?")    
    resultado = random.randint(1, D) + mod

if vant == "V":
    resultvant = max(resultado, resultado)
    print(resultvant)
elif vant == "D":
    resultdesv = min(resultado, resultado)
    print(resultdesv)
elif vant == "N":
    print(resultado)
else:
    print("Escolha uma opção valida")