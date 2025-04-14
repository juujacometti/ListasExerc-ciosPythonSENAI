import random

# Simule o lançamento de uma moeda até sair "cara" três vezes seguidas. (Dica: usar random.choice(["cara", "coroa"]) e while).

# Variáveis para contabilizar quantas vezes cada lado foi sorteado
cara = 0
coroa = 0

# Looping para verificar a quantidade de vezes que "cara" foi sorteado
while cara < 3:
    resultado = random.choice(["cara", "coroa"])
    print(resultado)
    
    # A cada sorteio, é contabilizado +1 para o lado que foi sorteado
    if  resultado == "cara":
        cara += 1
        
    else:
        coroa += 1
        
print(f"\nForam sorteados:\n{cara} vezes o lado Cara\n{coroa} vezes o lado Coroa")