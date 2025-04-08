# Peça 10 números e separe em duas listas: pares e ímpares. Mostre as duas no final.

# Criação da lista dos números pares e ímpares
pares = []
impares = []

# Looping (solicitação de 10 números)
for numero in range(10):
    valor = int(input("Informe um número inteiro para verificar se ele é par ou ímpar:\n"))

    # Se o número for par, o mesmo será adicionado na lista de números pares
    if valor % 2 == 0:
        pares.append(valor)

    # Se o número for ímpar, o mesmo será adicionado na lista de números ímpares
    else:
        impares.append(valor)

print(f"Os números digitados que são pares são:\n{pares}\nOs números digitados que são ímpares são:\n{impares}")