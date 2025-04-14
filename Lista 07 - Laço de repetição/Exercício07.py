# Peça uma frase e conte quantas vogais há nela. Mostre o total de cada uma (a, e, i, o, u).

# Solicitação da frase
frase = input("Digite uma frase para verificar quantas vogais existem nela:\n")

# Variáveis que contam o número de cada vogal separadamente
a = 0
e = 0
i= 0
o = 0
u = 0

print(f"\nNa frase \n  {frase}\nexistem:")

# Looping para verificar a quantidade de cada vogal existente na frase
for vogal in frase:
    if vogal == "a" or vogal == "A":
        a += 1
    
    if vogal == "e" or vogal == "E":
        e += 1

    if vogal == "i" or vogal == "I":
        i += 1
        
    if vogal == "o" or vogal == "O":
        o += 1
        
    if vogal == "u" or vogal == "U":
        u += 1
        
print(f"A: {a}\nE: {e}\nI: {i}\nO: {o}\nU: {u}")
    